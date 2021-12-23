class Solution:
    def minMoves(self, nums):
        return sum(nums) - len(nums) * min(nums)

    # 參考：https://www.itread01.com/content/1543972382.html
    # 假設陣列最後為某一個數為f，一共加了n次，陣列的長度為l，陣列中最小的數字為m
    # ，陣列和為s，f*l=s+(l-1)*n，f最小的情況是什麼，一定是陣列中的最小加了n，即
    # f=n+m，代入得n*l+m*l=s+l*n-n n=s-m*l
    
if __name__ == '__main__':
    s = Solution()
    print(s.minMoves([1, 2, 3]))