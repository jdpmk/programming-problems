// 1094
// Increasing Array
// https://cses.fi/problemset/task/1094
 
#include <algorithm>
#include <iostream>
 
int main(int argc, char** argv) {
    int n;
    std::cin >> n;
 
    long long nums[200000];
 
    for (size_t i = 0; i < n; ++i)
        std::cin >> nums[i];
 
    long long min_moves = 0;
    for (size_t i = 1; i < n; i++) {
        if (nums[i - 1] > nums[i]) {
            min_moves += nums[i - 1] - nums[i];
            nums[i] = nums[i - 1];
        }
    }
 
    std::cout << min_moves << std::endl;
 
    return 0;
}
