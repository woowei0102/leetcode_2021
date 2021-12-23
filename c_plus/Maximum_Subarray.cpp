#include <iostream>
#include <cmath>
#include <vector>

using namespace std; 

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int a = nums[0];
        int b = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            a = max(a + nums[i], nums[i]);
            b = max(a, b);
        }
        return b;
    }
};

int main() {
    Solution s;
    vector<int> l = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    cout << s.maxSubArray(l) << endl;
}