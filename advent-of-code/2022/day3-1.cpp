#include <fstream>
#include <iostream>
#include <unordered_set>
#include <vector>

char find_common(const std::string &sack) {
    size_t n = sack.length();
    std::unordered_set<char> seen;

    for (size_t i = 0; i < n / 2; i++) {
        seen.insert(sack[i]);
    }

    for (size_t i = n / 2; i < n; i++) {
        auto c_it = seen.find(sack[i]);
        if (c_it != seen.end()) {
            return sack[i];
        }
    }

    return '\0';
}

int solve(const std::vector<std::string> &sacks) {
    int total = 0;

    for (const auto &sack : sacks) {
        char common = find_common(sack);

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
