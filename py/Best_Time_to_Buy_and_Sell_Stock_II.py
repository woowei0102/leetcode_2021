class Solution:
    def maxProfit(self, prices):
        ans = [y - x for x, y in zip(prices[0:-1], prices[1:]) if x < y]
        return sum(ans)

        # max_profit = 0
        # for i in range(1, len(preices)):
        #     if (prices[i] > prices[i - 1]):
        #         max_profit += prices[i] > prices[i - 1]
        # return max_profit
        
if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))