class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        ls = len(nums)
        n_pos = 0
        for i in range(ls):
            if nums[i] != 0:
                temp = nums[n_pos]
                nums[n_pos] = nums[i]
                nums[i] = temp
                n_pos += 1

if __name__ == '__main__':
    s = Solution()
    print(s.moveZeroes([0, 1, 0, 3, 12]))