// 1069
// Repetitions
// https://cses.fi/problemset/task/1069
 
#include <algorithm>
#include <iostream>
 
int main(int argc, char** argv) {
    std::string s;
    getline(std::cin, s);
 
    int longest = 1;
    int current = 1;
 
    for (size_t i = 1; i < s.length(); ++i) {
        if (s[i] == s[i - 1])
            current += 1;
        else
            current = 1;
 
        longest = std::max(longest, current);        
    }
 
    std::cout << longest << std::endl;
 
    return 0;
}
