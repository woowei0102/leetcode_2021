class Solution:
    def readBinaryWatch(self, turnedOn):
        return ['%d:%02d' % (h, m)
            for h in range(12) for m in range(60)
            if (bin(h) + bin(m)).count('1') == turnedOn]

if __name__ == '__main__':
    s = Solution()
    print(s.readBinaryWatch(1))