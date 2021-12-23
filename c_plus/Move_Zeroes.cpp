class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int l = nums.size();
        int pos = 0;
        for (int i = 0; i < l; i++) {
            if (nums[i] != 0) {
                int temp = nums[pos];
                nums[pos] = nums[i];
                nums[i] = temp;
                pos++;
            }
        }
    }
};