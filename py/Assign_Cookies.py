class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        child = 0
        cookie = 0
        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                child += 1
            cookie += 1
        return child


if __name__ == '__main__':
    s = Solution()
    print(s.findContentChildren([1, 2, 3], [1, 1]))