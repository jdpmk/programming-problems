#include <iostream>

int main() {
    long long n, x;
    std::cin >> n;

    int total = n * (n + 1) / 2;

    for (int i = 0; i < n - 1; i++) {
        std::cin >> x;
        total -= x;
    }

    std::cout << total << std::endl;

    return 0;
}
