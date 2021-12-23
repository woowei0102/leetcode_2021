class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lsa, lsb = len(a), len(b)
        res = carry = 0
        count = 0
        while lsa > 0 or lsb > 0:
            if lsa <= 0:
                x = 0
            else:
                x = int(a[lsa - 1])
                lsa -= 1
            if lsb <= 0:
                y = 0
            else:
                y = int(b[lsb - 1])
                lsb -= 1
            res = res + ((x + y + carry) % 2) * (10 ** count)
            carry = (x + y + carry) // 2
            count += 1
        if carry > 0:
            res += 10 ** count
        return str(res)

if __name__ == '__main__':
    s = Solution()
    print(s.addBinary("11", "1"))
