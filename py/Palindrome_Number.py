class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if (x == x[::-1]):
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))