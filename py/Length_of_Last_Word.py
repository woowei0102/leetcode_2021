class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        temp = s.split()
        return len(temp[-1])

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord("   fly me   to   the moon  "))