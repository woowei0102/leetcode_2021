class Solution:
    def reverseBits(self, nums):
        b = bin(nums)[: 1 : -1]
        return int(b + '0' * (32 - len(b)), 2)

if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(43261596))
    # s = [1, 2, 3, 4, 5]
    # print(s[: 1 : -1])