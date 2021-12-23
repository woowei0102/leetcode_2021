from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        left = 0
        for i in range(1, len(nums)):
            if nums[left] == nums[i]:
                continue
            else:
                left += 1
                nums[left] = nums[i]
            print(nums)
        return left + 1

if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,1,2]))