#include <iostream>

int main() {
    int n;
    std::cin >> n;

    if (n == 1) {
        std::cout << 1 << std::endl;
    } else if (n <= 3) {
        std::cout << "NO SOLUTION" << std::endl;
    } else {
        for (int i = 2; i <= n; i += 2) {
            std::cout << i << " ";
        }
        for (int i = 1; i <= n; i += 2) {
            std::cout << i << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}
