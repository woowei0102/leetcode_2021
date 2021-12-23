class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        # letter map
        mp = '0123456789abcdef'
        ans = ''
        for _ in range(8):
            # get last 4 digits
            # num & 1111b
            n = num & 15 # num % 16
            # hex letter for current 1111
            c = mp[n]
            ans = c + ans
            # num = num / 16
            num = num >> 4
        #strip leading zeroes
        return ans.lstrip('0')

if __name__ == '__main__':
    s = Solution()
    print(s.toHex(26))