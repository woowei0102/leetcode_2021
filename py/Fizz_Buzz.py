class Solution:
    def fizzBuzz(self, n):
        res = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                res.append('FizzBuzz')
            elif i % 3 == 0:
                res.append('Fizz')
            elif i % 5 == 0:
                res.append('Buzz')
            else:
                res.append('%d' % (i))
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.fizzBuzz(3))