class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 1, num
        while low <= high:
            mid = (low + high) / 2
            mid_square = mid * mid
            if mid_square == num:
                return True
            elif mid_square < num:
                low = mid + 1
            else:
                high = mid - 1
        return False
