class NumArray():
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.res = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.res[i + 1] = self.res[i] + nums[i]


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.res[j + 1] - self.res[i]