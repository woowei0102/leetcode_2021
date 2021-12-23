class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s1 = t1 = 0
        while s1 < len(s) and t1 < len(t):
            if t[t1] == s[s1]:
                s1 += 1
            t1 += 1
        return s1 == len(s)