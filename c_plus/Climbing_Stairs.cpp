#include <iostream>
using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        if (n <= 1) return 1;
        int dp[2] = {1, 1};
        for (int i = 2; i < n + 1; i++) {
            int temp = dp[1];
            dp[1] = dp[1] + dp[0];
            dp[0] = temp;
        }
        return dp[1];
    }
};

int main() {
    Solution s;
    cout << s.climbStairs(4) << endl;
}