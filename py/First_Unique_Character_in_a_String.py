class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        count_map = {}
        for c in s:
            count_map[c] = count_map.get(c, 0) + 1
        for i, c in enumerate(s):
            if count_map[c] == 1:
                return i
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.firstUniqChar('leetcode'))