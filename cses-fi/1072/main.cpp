#include <iostream>

int main() {
    unsigned long long n, ans;
    std::cin >> n;

    for (unsigned long long k = 1; k <= n; k++) {
        ans = (k * k) * (k * k - 1) / 2 - 8 * (k - 1) * (k - 2) / 2;
        std::cout << ans << std::endl;
    }

    return 0;
}
