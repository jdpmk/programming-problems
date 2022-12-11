#include <cstdio>
#include <fstream>
#include <functional>
#include <iostream>
#include <queue>
#include <string>

constexpr int NUM_ROUNDS = 10000;

std::vector<std::string> split(std::string s,
                               const std::string &delimiter)
{
    std::vector<std::string> items;
    size_t pos = 0;

    while ((pos = s.find(delimiter)) != std::string::npos) {
        std::string token = s.substr(0, pos);
        items.push_back(std::move(token));
        s.erase(0, pos + delimiter.length());
    }

    items.push_back(std::move(s));

    return items;
}

struct monkey_t {
    std::queue<long long> items;
    std::function<long long(long long, long long)> op;
    std::pair<long long, long long> arg;
    int mod;
    int true_branch_dst;
    int false_branch_dst;
    int items_inspected;

    monkey_t(const std::vector<std::string> &group) {
        char items_buf[256] = {0};
        char arg1_buf[256] = {0};
        char arg2_buf[256] = {0};
        char op_buf[2] = {0};

        std::sscanf(group[0].c_str(), "Starting items: %[^\t]", items_buf);
        std::sscanf(group[1].c_str(), "Operation: new = %s %s %s", arg1_buf, op_buf, arg2_buf);
        std::sscanf(group[2].c_str(), "Test: divisible by %d", &mod);
        std::sscanf(group[3].c_str(), "If true: throw to monkey %d", &true_branch_dst);
        std::sscanf(group[4].c_str(), "If false: throw to monkey %d", &false_branch_dst);

        std::string items_str(items_buf);
        std::vector<std::string> items_vec = split(items_str, ", ");
        for (const auto &item : items_vec) items.push(std::stoi(item));

        if (!strcmp(arg1_buf, "old")) arg.first = -1; else arg.first = std::stoi(arg1_buf);
        if (!strcmp(arg2_buf, "old")) arg.second = -1; else arg.second = std::stoi(arg2_buf);
        if (!strcmp(op_buf, "+")) op = std::plus<long long>();
        if (!strcmp(op_buf, "*")) op = std::multiplies<long long>();

        items_inspected = 0;
    }
};

std::vector<std::unique_ptr<monkey_t>> read(const std::vector<std::string> &lines) {
    std::vector<std::unique_ptr<monkey_t>> monkeys;

    for (size_t i = 0; i < lines.size(); i += 6) {
        std::vector<std::string> group(lines.begin() + i + 1, lines.begin() + i + 6);
        monkeys.push_back(std::make_unique<monkey_t>(std::move(group)));
    }

    return monkeys;
}

long long solve(std::vector<std::unique_ptr<monkey_t>> &monkeys) {
    int mod = 1;
    for (auto &&monkey_ptr : monkeys) {
        mod *= monkey_ptr->mod;
    }

    for (int i = 0; i < NUM_ROUNDS; i++) {
        for (auto &&monkey_ptr : monkeys) {
            if (monkey_ptr->items.empty()) continue;

            while (!monkey_ptr->items.empty()) {
                auto item = monkey_ptr->items.front();
                monkey_ptr->items.pop();

                auto [arg1, arg2] = monkey_ptr->arg;
                auto updated = monkey_ptr->op(
                    arg1 == -1 ? item : arg1,
                    arg2 == -1 ? item : arg2);

                updated %= mod;

                auto dst = updated % monkey_ptr->mod == 0
                    ? monkey_ptr->true_branch_dst
                    : monkey_ptr->false_branch_dst;

                monkeys[dst]->items.push(updated);
                monkey_ptr->items_inspected++;
            }
        }
    }

    std::vector<long long> all_items_inspected;
    for (auto &&monkey_ptr : monkeys) {
        all_items_inspected.push_back(monkey_ptr->items_inspected);
    }

    std::sort(all_items_inspected.begin(), all_items_inspected.end(),
              [] (const long long a, const long long b) {
                  return a > b;
              });

    return all_items_inspected[0] * all_items_inspected[1];
}

int main() {
    std::ifstream input("input/11.data");

    std::vector<std::string> lines;
    while (input.good()) {
        std::string line;
        std::getline(input, line);
        if (!line.empty()) {
            lines.push_back(std::move(line));
        }
    }

    input.close();

    auto monkeys = read(lines);
    std::cout << solve(monkeys) << std::endl;

    return 0;
}
