class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int res = nums[0];
        int cnt = 1;
        int l = nums.size();
        for (int i = 1; i < l; i++) {
            if (res == nums[i]) cnt++;
            else if (cnt > 0) cnt--;
            else {
                res = nums[i];
                cnt += 1;
            }
        }
        return res;
    }
};