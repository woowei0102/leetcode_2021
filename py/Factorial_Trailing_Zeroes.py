class Solution:
    def trailingZeroes(self, n: int) -> int:
        ## method 1
        # res = 1
        # for i in range(n, 0, -1):
        #     res *= i
        # ans = 0
        # while res % 10 == 0:
        #     ans += 1
        #     res //= 10
        # return ans

        ## method 2
        cnt = 0
        while n >= 5:
            cnt += n // 5
            n //= 5
        return cnt

if __name__ == '__main__':
    s = Solution()
    print(s.trailingZeroes(6))
    # 6 5 4 3 2 1