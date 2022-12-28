#include <algorithm>
#include <iostream>

int main() {
    int n;
    std::cin >> n;

    int max_so_far = 0;
    int x = 0;
    long long moves = 0;

    for (int i = 0; i < n; i++) {
        std::cin >> x;
        if (x < max_so_far) {
            moves += max_so_far - x;
        }
        max_so_far = std::max(max_so_far, x);
    }

    std::cout << moves << std::endl;

    return 0;
}
