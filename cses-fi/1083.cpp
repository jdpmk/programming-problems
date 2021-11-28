// 1083
// Missing Number
// https://cses.fi/problemset/task/1083
 
#include <iostream>
 
int main(int argc, char** argv) {
    long long n;
    std::cin >> n;
 
    long long sum = n * (n + 1) / 2;
    long long x;
 
    for (size_t i = 0; i < n - 1; i++) {
        std::cin >> x;
        sum -= x;
    }
 
    std::cout << sum << std::endl;
 
    return 0;
}
