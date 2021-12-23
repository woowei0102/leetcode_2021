from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxEndingHere = maxSofFar = nums[0]
        for i in range(1, len(nums)):
            maxEndingHere = max(maxEndingHere + nums[i], nums[i])
            maxSofFar = max(maxEndingHere, maxSofFar)
        return maxSofFar

if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))