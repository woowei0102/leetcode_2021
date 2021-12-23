class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = ord(t[-1])
        for i in range(len(s)):
            res += ord(t[i])
            res -= ord(s[i])
        return chr(res)

if __name__ == '__main__':
    s = Solution()
    print(s.findTheDifference('abcd', 'abcde'))