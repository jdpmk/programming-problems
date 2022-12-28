#include <algorithm>
#include <iostream>

int main() {
    int t;
    std::cin >> t;

    for (int i = 0; i < t; i++) {
        unsigned long long a, b;
        std::cin >> a >> b;

        if (a > b) {
            std::swap(a, b);
        }

        if (b > 2 * a) {
            std::cout << "NO" << std::endl;
        } else {
            if ((a % 3 == 1 && b % 3 == 2) ||
                (a % 3 == 2 && b % 3 == 1) ||
                (a % 3 == 0 && b % 3 == 0))
            {
                std::cout << "YES" << std::endl;
            } else {
                std::cout << "NO" << std::endl;
            }
        }
    }

    return 0;
}
