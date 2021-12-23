class Solution:
    def singleNumber(self, nums):
        ## method 1
        # res = 0
        # for i in nums:
        #     res ^= i
        # return res

        ## method 2
        res = []
        for i in nums:
            if i in res:
                res.remove(i)
            else:
                res.append(i)
        return res[0]

if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([1, 2, 2]))
