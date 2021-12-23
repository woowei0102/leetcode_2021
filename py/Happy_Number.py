class Solution:
    def isHappy(self, n: int) -> bool:
        if n < 1:
            return False
        seed = set()
        while n != 1:
            temp = 0
            if n in seed:
                return False
            else:
                seed.add(n)
            while n != 0:
                temp += (n % 10) ** 2
                n //= 10
            n = temp
        return n == 1

        


if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(19))
    