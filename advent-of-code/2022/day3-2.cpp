#include <fstream>
#include <iostream>
#include <set>
#include <unordered_map>
#include <vector>

char find_common(const std::string &sack1,
                 const std::string &sack2,
                 const std::string &sack3)
{
    std::unordered_map<char, int> freq;

    std::set<char> types1(sack1.begin(), sack1.end());
    std::set<char> types2(sack2.begin(), sack2.end());
    std::set<char> types3(sack3.begin(), sack3.end());

    for (char item_type : types1) freq[item_type]++;
    for (char item_type : types2) freq[item_type]++;
    for (char item_type : types3) freq[item_type]++;

    for (const auto [item_type, item_type_freq] : freq) {
        if (item_type_freq == 3) {
            return item_type;
        }
    }

    return '\0';
}

int solve(const std::vector<std::string> &sacks) {
    int total = 0;

    for (size_t i = 0; i < sacks.size(); i += 3) {
        int common = find_common(sacks[i], sacks[i + 1], sacks[i + 2]);

        if (std::islower(common)) {
            total += static_cast<int>(common) - 96; 
        } else if (std::isupper(common)) {
            total += static_cast<int>(common) - 38;
        } else {
            exit(1);
        }
    }

    return total;
}

int main() {
    std::ifstream input("input/3.data");
    std::vector<std::string> sacks;

    while (input.good()) {
        std::string line;
        std::getline(input, line);
        if (!line.empty()) {
            sacks.push_back(std::move(line));
        }
    }

    std::cout << solve(sacks) << std::endl;

    return 0;
}
