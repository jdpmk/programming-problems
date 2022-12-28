#include <cmath>
#include <iostream>

int main() {
    unsigned long long n;
    std::cin >> n;

    unsigned long long ans = 1;

    for (unsigned long long i = 0; i < n; i++) {
        ans = (ans * 2) % 1000000007;
    }

    std::cout << ans << std::endl;

    return 0;
}
