#include <iostream>
#define INT_MAX     2147483647
#define INT_MIN     (-INT_MAX - 1)

using namespace std;

class Solution {
public:
    int reverse(int x) {
    
        int res = 0;
        while (x != 0) {

            if (res > INT_MAX / 10 || res < INT_MIN / 10)
                return 0;
            res = res * 10 + x % 10;
            x /= 10;
        }
        return res;
    }
};

int main() {
    Solution s;
    int ans = s.reverse(-123);
    cout << ans << endl;
}