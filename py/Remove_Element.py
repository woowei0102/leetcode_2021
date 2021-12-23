from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ls = len(nums)
        if ls == 0:
            return ls
        count = 0
        index = 0
        while index < ls - count:
            if nums[index] == val:
                nums[index] = nums[ls - 1 - count]
                count += 1
            else:
                index += 1
            print(nums)
        return ls - count

            
if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([3,2,2,3], 3))