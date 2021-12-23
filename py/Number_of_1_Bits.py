class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count



        ## method 2?
        # nums = str(n)
        # count = 0
        # for i in range(len(nums)):
        #     if nums[i] == '1':
        #         count += 1
        # return count

if __name__ == '__main__':
    s = Solution()
    print(s.hammingWeight(1011))

    # 1101 1100 1000 0000
    # 1100 1011 0111