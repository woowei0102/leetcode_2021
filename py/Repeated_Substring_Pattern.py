class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sl = len(s)
        for i in range(1, sl // 2 + 1):
            if sl % i == 0:
                if s[:i] * (sl // i) == s:
                    return True
        return False