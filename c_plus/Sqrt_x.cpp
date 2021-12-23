#include <iostream>
using namespace std;

class Solution {
public:
    int mySqrt(int x) {
        if (x == 0) return 0;
        if (x < 4) return 1;
        long res = 2 * mySqrt(x / 4);
        if ((res + 1) * (res + 1) <= x) return res + 1;
        return res;
    }
};

int main() {
    Solution s;
    cout << s.mySqrt(16) << endl;
}