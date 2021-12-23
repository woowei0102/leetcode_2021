class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        dp = [1] * 2
        for i in range(2, n + 1):
            dp[1], dp[0] = dp[1] + dp[0], dp[1]
        return dp[1]

if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(5))