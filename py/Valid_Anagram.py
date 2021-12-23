class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = [ord(i) - ord('a') for i in s]
        s2 = [ord(j) - ord('a') for j in t]
        s1.sort()
        s2.sort()
        return s1 == s2
        


if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))