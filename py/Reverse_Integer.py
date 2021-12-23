class Solution:
    def reverse(self, x: int) -> int:
        neg, res= 1, 0
        if x < 0:
            neg = -1
            x = x * -1
        while x != 0:
            res = res * 10 + x % 10
            # leetcode 無法檢測出大於(2^31 -1)的數字，無論輸入輸出
            if res > 2147483647:
                return 0
            x = x // 10
        return res * neg

if __name__ == '__main__':
    s = Solution()
    print(s.reverse(1534236469))