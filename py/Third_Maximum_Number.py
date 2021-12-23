class Solution:
    def thirdMax(self, nums):
        nums_set = set(nums)
        if len(nums_set) < 3:
            return max(nums_set)
        nums_set.remove(max(nums_set))
        nums_set.remove(max(nums_set))
        return max(nums_set)


if __name__ == '__main__':
    s = Solution()
    print(s.thirdMax([3,2,1]))