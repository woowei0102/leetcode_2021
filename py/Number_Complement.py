class Solution:
    def findComplement(self, num: int) -> int:
        bin_num = bin(num)[2:]
        res = ''
        for i in bin_num:
            res += str(1 - int(i))
        return int(res, 2)

if __name__ == '__main__':
    s = Solution()
    print(s.findComplement(1))
