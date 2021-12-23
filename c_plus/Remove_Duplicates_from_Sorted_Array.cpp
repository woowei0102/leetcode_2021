# include <iostream>
# include <vector>
using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        int pos = 0;
        for (int i = 1; i < nums.size(); i++)
            if (nums[pos] == nums[i]) 
                continue;
            else 
                nums[++pos] = nums[i];
        return pos + 1;
    }
};

int main() {
    Solution s;
    vector<int> numbers = {0,0,1,1,1,2,2,3,3,4};
    int ans = s.removeDuplicates(numbers);
    cout << ans << endl;
}