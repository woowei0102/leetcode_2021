class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * n
        for i in range(2, n):
            if i * i >= n:
                break
            if not isPrime[i]:
                continue
            for j in range(i * i, n, i):
                isPrime[j] = False
        count = 0
        for i in range(2, n):
            if isPrime[i]:
                count += 1
        return count

        ## method 2
        # count = 0
        # for num in range(n):
        #     if num > 1:
        #         for i in range(2, num):
        #             if (num % i) == 0:
        #                 break
        #     else:
        #         count = count + 1
        # return count

if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes(10))
