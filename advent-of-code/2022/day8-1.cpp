#include <fstream>
#include <iostream>
#include <vector>

bool visible_from_top(const std::vector<std::string> &forest,
                      size_t ci, size_t cj)
{
    for (size_t i = 0; i < ci; i++) {
        if (forest[i][cj] >= forest[ci][cj]) {
            return false;
        }
    }

    return true;
}

bool visible_from_bottom(const std::vector<std::string> &forest,
                         size_t ci, size_t cj)
{
    size_t m = forest.size();
    for (size_t i = m - 1; i > ci; i--) {
        if (forest[i][cj] >= forest[ci][cj]) {
            return false;
        }
    }

    return true;
}

bool visible_from_left(const std::vector<std::string> &forest,
                       size_t ci, size_t cj)
{
    for (size_t j = 0; j < cj; j++) {
        if (forest[ci][j] >= forest[ci][cj]) {
            return false;
        }
    }

    return true;
}


bool visible_from_right(const std::vector<std::string> &forest,
                        size_t ci, size_t cj)
{
    size_t n = forest[0].size();
    for (size_t j = n - 1; j > cj; j--) {
        if (forest[ci][j] >= forest[ci][cj]) {
            return false;
        }
    }

    return true;
}

int solve(const std::vector<std::string> &forest) {
    size_t m = forest.size();
    size_t n = forest[0].size();

    int total = n * 2 + (m - 2) * 2;

    for (size_t i = 1; i < m - 1; i++) {
        for (size_t j = 1; j < n - 1; j++) {
            if (visible_from_top(forest, i, j) ||
                visible_from_bottom(forest, i, j) ||
                visible_from_left(forest, i, j) ||
                visible_from_right(forest, i, j))
            {
                total++;
            }
        }
    }

    return total;
}

int main() {
    std::ifstream input("input/8.data");

    std::vector<std::string> forest;
    while (input.good()) {
        std::string line;
        std::getline(input, line);
        if (!line.empty()) {
            forest.push_back(std::move(line));
        }
    }

    input.close();

    std::cout << solve(forest) << std::endl;

    return 0;
}
