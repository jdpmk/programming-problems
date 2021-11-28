// 1070
// Permutations
// https://cses.fi/problemset/task/1070
 
#include <iostream>
 
int main(int argc, char** argv) {
    /*
      n = 1: YES; 1
      n = 2: NO
      n = 3: NO
      n = 4: NO
      n = 5: YES; 1 3 5 2 4
      n = 6: YES; 1 3 5 2 4 6 
      n = 7: YES; 1 3 5 7 2 4 6
      n = 8: YES; 1 3 5 7 2 4 6 8
      ...
    */
 
    int n;
    std::cin >> n;
 
    if (n == 1) {
        std::cout << 1 << std::endl;
    } else if (n == 2 || n == 3) {
        std::cout << "NO SOLUTION" << std::endl;
    } else {
        for (int i = 2; i <= n; i += 2) {
            std::cout << i << " ";
        }
        for (int i = 1; i <= n; i += 2) {
            if (i + 2 > n)
                std::cout << i << std::endl;
            else
                std::cout << i << " ";
        }
    }
 
    return 0;
}
