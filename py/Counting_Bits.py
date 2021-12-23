class Solution:
    def countBits(self, n: int):
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.countBits(2))
    # for i in range(1,8):
    #     print(' ' * (7 - i) + '*' * (2 * i - 1))
