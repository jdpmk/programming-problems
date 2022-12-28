#include <iostream>
#include <vector>
#include <unordered_set>

int main() {
    unsigned long long n;
    std::cin >> n;

    unsigned long long total = n * (n + 1) / 2;

    if (total % 2 == 1) {
        std::cout << "NO" << std::endl;
    } else {
        std::vector<unsigned long long> a;
        std::vector<unsigned long long> b;

        unsigned long long a_tot = 0;
        
        for (unsigned long long i = n; i >= 1; i--) {
            if (a_tot + i > total / 2) {
                b.push_back(i);
            } else {
                a_tot += i;
                a.push_back(i);
            }
        }

        std::cout << "YES" << std::endl;

        std::cout << a.size() << std::endl;
        for (auto x : a) {
            std::cout << x << " ";
        }
        std::cout << std::endl;

        std::cout << b.size() << std::endl;
        for (auto x : b) {
            std::cout << x << " ";
        }
        std::cout << std::endl;
    }

    return 0;
}
