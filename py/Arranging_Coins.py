class Solution:
    def arrangeCoins(self, n: int) -> int:
        res = 0
        coin = n
        i = 1
        while True:
            res += 1
            coin -= i
            if coin < 0:
                return res -1
            i += 1



if __name__ == '__main__':
    s = Solution()
    print(s.arrangeCoins(8))