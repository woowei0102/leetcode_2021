from _typeshed import IdentityFunction


class Solution:
    def summaryRanges(self, nums):
        res = []
        s, ls = 0, len(nums)
        for i in range(ls):
            if i + 1 < ls and nums[i + 1] == nums[i] + 1:
                continue
            if i == s:
                res.append(str(nums[s]))
            else:
                res.append("%d->%d" % (nums[s], nums[i]))
            s = i + 1
        return res
        