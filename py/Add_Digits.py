from typing import NamedTuple


class Solution:
    def addDigits(self, num: int) -> int:
        ## method 1
        # if num < 10:
        #     return num
        # return num - ((num - 1) // 9) * 9

        ## method 2
        # while num >= 10:
        #     num = (num // 10) + (num % 10)
        # return num
        
        ## method 3
        if num < 10:
            return num
        return 1 + (num - 1) % 9

if __name__ == '__main__':
    s = Solution()
    print(s.addDigits(38))