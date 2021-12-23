class Solution:
    def longestPalindrome(self, s: str) -> int:
        ct = set(s)
        res = 0
        f = 0
        for v in ct:
            if s.count(v) % 2 == 0:
                res += s.count(v)
            else:
                res += s.count(v) - 1
                f = 1
        return res + f

if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("abccccdd"))