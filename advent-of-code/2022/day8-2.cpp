#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

int top_viewing_distance(const std::vector<std::string> &forest,
                         int ci, int cj)
{
    int seen = 0;

    for (int i = ci - 1; i >= 0; i--) {
        seen++;
        if (forest[i][cj] >= forest[ci][cj]) {
            break;
        }
    }

    return seen;
}

int bottom_viewing_distance(const std::vector<std::string> &forest,
                            int ci, int cj)
{
    size_t m = forest.size();
    int seen = 0;

    for (int i = ci + 1; i < m; i++) {
        seen++;
        if (forest[i][cj] >= forest[ci][cj]) {
            break;
        }
    }

    return seen;
}

int left_viewing_distance(const std::vector<std::string> &forest,
                          int ci, int cj)
{
    int seen = 0;

    for (int j = cj - 1; j >= 0; j--) {
        seen++;
        if (forest[ci][j] >= forest[ci][cj]) {
            break;
        }
    }

    return seen;
}

int right_viewing_distance(const std::vector<std::string> &forest,
                           int ci, int cj)
{
    size_t n = forest[0].size();
    int seen = 0;

    for (int j = cj + 1; j < n; j++) {
        seen++;
        if (forest[ci][j] >= forest[ci][cj]) {
            break;
        }
    }

    return seen;
}

int solve(const std::vector<std::string> &forest) {
    size_t m = forest.size();
    size_t n = forest[0].size();

    int max_scenic_score = std::numeric_limits<int>::min();

    for (size_t i = 1; i < m - 1; i++) {
        for (size_t j = 1; j < n - 1; j++) {
            int top = top_viewing_distance(forest, i, j);
            int bottom = bottom_viewing_distance(forest, i, j);
            int left = left_viewing_distance(forest, i, j);
            int right = right_viewing_distance(forest, i, j);

            int scenic_score = top * bottom * left * right;
            max_scenic_score = std::max(max_scenic_score, scenic_score);
        }
    }

    return max_scenic_score;
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
