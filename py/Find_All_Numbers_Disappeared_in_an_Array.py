class Solution:
    def findDisappearedNumbers(self, nums):
        nums_set = set(nums)
        res = []
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                res.append(i)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))