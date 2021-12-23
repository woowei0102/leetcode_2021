from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ls = len(digits)
        for index in reversed(range(ls)):
            if digits[index] < 9:
                digits[index] += 1
                # do not need to continue
                return digits
            else:
                # 10
                digits[index] = 0
        digits.insert(0, 1)
        return digits

if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([1,2,3]))