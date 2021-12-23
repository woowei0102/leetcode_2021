class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0 or n > 1162261467:
            return False
        while n != 1:
            if n % 3 != 0:
                return False
            n //= 3
        return  n == 1

if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfThree(9))