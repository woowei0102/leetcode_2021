class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        pos1, pos2 = len(num1) - 1, len(num2) - 1
        carry = 0
        res = []
        while pos1 >= 0 or pos2 >= 0 or carry == 1:
            dig1 = dig2 = 0
            if pos1 >= 0:
                dig1 = ord(num1[pos1]) - ord('0')
            if pos2 >= 0:
                dig2 = ord(num2[pos2]) - ord('0')
            res.append(str((dig1 + dig2 + carry) % 10))
            carry = (dig1 + dig2 + carry) // 10
            pos1 -= 1
            pos2 -= 1
        return ''.join(res[::-1])
