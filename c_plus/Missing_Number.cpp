class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int s1 = 0;
        int s2 = 0;
        for (int i = 0; i < nums.size(); i++) {
            s1 += i;
            s2 += nums[i];
        }
        return s1 - s2 + nums.size();
    }
};