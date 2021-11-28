// 1068
// Weird Algorithm
// https://cses.fi/problemset/task/1068
 
#include <iostream>
 
int main(int argc, char** argv) {
    long long n;
    std::cin >> n;
 
    while (n != 1) {
        std::cout << n << " ";
        if (n % 2 == 0)
            n /= 2;
        else
            n = 3 * n + 1;
    }
 
    std::cout << 1 << std::endl;
 
    return 0;
}
