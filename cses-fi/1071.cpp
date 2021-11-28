// 1071
// Number Spiral
// https://cses.fi/problemset/task/1071
 
#include <iostream>
 
long int mat(long int y, long int x) {
    if (y > x)
        return (y / 2 * 2) * (y / 2 * 2) + (y % 2) + (y % 2 == 0 ? -1 : 1) * (x - 1);
    else
        return (x - (1 - x % 2)) * (x - (1 - x % 2)) + (1 - x % 2) + (x % 2 == 1 ? -1 : 1) * (y - 1);
}
 
int main(int argc, char** argv) {
    int t;
    std::cin >> t;
 
    long int y, x;
    while (t--) {
        std::cin >> y >> x;
        std::cout << (long int) mat(y, x) << std::endl;
    }
 
    return 0;
}
