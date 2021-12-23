from os import wait3
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = int(0), len(nums) - 1
        while l < r:
            mid = int((l + r) / 2)
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if nums[l] < target:
            return l + 1
        return l

if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 5))