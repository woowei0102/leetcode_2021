class Solution:
    def majorityElement(self, nums):
        res, cnt, l = nums[0], 1, len(nums)
        for i in range(1, l):
            if res == nums[i]:
                cnt += 1
            elif cnt > 0:
                cnt -= 1
            else:
                res = nums[i]
                cnt += 1
        return res