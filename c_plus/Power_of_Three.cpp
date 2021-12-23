#include<iostream>
using namespace std;

class Solution {
public:
    bool isPowerOfThree(int n) {
        if (n <= 0 or n > 1162261467) return false;
        while (n != 1) {
            if (n % 3 != 0) return false;
            n /= 3;
        }
        return n == 1;
    }
};

int main() {
    Solution s;
    cout << s.isPowerOfThree(45) << endl;
}
