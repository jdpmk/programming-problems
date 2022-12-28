#include <iostream>

int main() {
    unsigned long long n;
    std::cin >> n;

    unsigned long long divisor = 5;
    unsigned long long ans = 0;

    while (divisor <= n) {
        ans += n / divisor;
        divisor *= 5;
    }

    std::cout << ans << std::endl;

    return 0;
}
