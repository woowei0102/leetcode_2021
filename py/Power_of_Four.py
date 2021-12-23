class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0 or n > 1162261467:
            return False
        while n != 1:
            if n % 4 != 0:
                return False
            n //= 4
        return  n == 1