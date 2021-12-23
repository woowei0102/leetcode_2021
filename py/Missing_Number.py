class Solution:
    def missingNumber(self, nums):
        ## method 1
        # nums.sort()
        # pre = nums[0]
        # for i in range(1, len(nums)):
        #     if nums[i] != pre + 1:
        #         return pre + 1
        #     else:
        #         pre = nums[i]
        # if 0 in nums:
        #     return pre + 1
        # else:
        #     return 0

        ## method 2
        # s1 = s2 = 0
        # for i in range(len(nums)):
        #     s1 += i
        #     s2 += nums[i]
        # return s1 - s2 + len(nums)

        ## method 3
        res = len(nums)
        for i in range(len(nums)):
            res ^= i
            res ^= nums[i]
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([3, 0, 1]))

