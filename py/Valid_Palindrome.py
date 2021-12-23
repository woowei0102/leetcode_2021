class Solution:
    def isPalindrome(self, s: str) -> bool:

        ## method 1
        # nums = [t.lower() for t in s if t.isalnum()]
        # ls = len(nums)
        # if ls <= 1:
        #     return True
        # mid = ls // 2
        # if ls % 2 != 0:
        #     if nums[0 : mid] == list(reversed(nums[mid + 1 : ls])):
        #         return True
        #     else:
        #         return False
        # else:
        #     if nums[0 : mid] == list(reversed(nums[mid : ls])):
        #         return True
        #     else:
        #         return False

        ## method 2
        # nums = [t.lower() for t in s if t.isalnum()]
        # ls = len(nums)
        # if ls <= 1:
        #     return True
        # mid = ls // 2
        # if ls % 2 != 0:
        #     if nums[0 : mid] == nums[ls - 1 : mid : -1]:
        #         return True
        #     else:
        #         return False
        # else:
        #     if nums[0 : mid] == nums[ls - 1 : mid - 1: -1]:
        #         return True
        #     else:
        #         return False

        ## method 3
        alnum_s = [t.lower() for t in s if t.isalnum()]
        ls = len(alnum_s)
        if ls <= 1:
            return True
        mid = ls // 2
        for i in range(mid):
            if alnum_s[i] != alnum_s[ls - 1 - i]:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome("12321"))
#   *
# 1221
# 0123