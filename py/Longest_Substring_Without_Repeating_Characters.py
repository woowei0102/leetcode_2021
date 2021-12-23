class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # https://leetcode.com/articles/longest-substring-without-repeating-characters/
        charMap = [-1 for i in range(256)]
        ls = len(s)
        i = max_len = 0
        for j in range(ls):
            # Note that when charMap[ord(s[j])] >= i, it means that there are
            # duplicate character in current i,j. So we need to update i.
            if charMap[ord(s[j])] >= i:
                i = charMap[ord(s[j])] + 1
            charMap[ord(s[j])] = j
            max_len = max(max_len, j - i + 1)
        return max_len

if __name__ == '__main__':
    s = Solution()
    str1 = "pwwkew"
    print(s.lengthOfLongestSubstring(str1))
