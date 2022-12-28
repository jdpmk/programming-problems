#include <iostream>

int main() {
    int t;
    std::cin >> t;

    for (int i = 0; i < t; i++) {
        unsigned long long y, x, ans;
        std::cin >> y >> x;

        if (y == x) {
            ans = y * y - (y - 1);
        } else if (y > x) {
            if (y % 2 == 0) {
                ans = y * y - (x - 1);
            } else {
                ans = (y - 1) * (y - 1) + 1 + (x - 1);
            }
        } else {
            if (x % 2 == 0) {
                ans = (x - 1) * (x - 1) + 1 + (y - 1);
            } else {
                ans = x * x - (y - 1);
            }
        }

        std::cout << ans << std::endl;
    }

    return 0;
}
