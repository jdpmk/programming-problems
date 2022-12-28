#include <algorithm>
#include <iostream>

int main() {
    std::string s;
    std::cin >> s;

    int current_length = 1;
    int max_length = 1;

    for (size_t i = 1; i < s.length(); i++) {
        if (s[i] == s[i - 1]) {
            current_length++;
        } else {
            current_length = 1;
        }

        max_length = std::max(max_length, current_length);
    }

    std::cout << max_length << std::endl;

    return 0;
}
