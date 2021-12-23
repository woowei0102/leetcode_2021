class Solution:
    def titleToNumber(self, columnTitle):
        ## method 1
        result = 0
        n = len(columnTitle)
        for i in range(n):
            result = result * 26 + ord(columnTitle[i]) - 64
        return result

        ## method 2
        # if len(columnTitle) == 1:
        #     return ord(columnTitle)-64
        # return ord(columnTitle[-1]) - 64 + 26 * \
        #         self.titleToNumber(columnTitle[:-1]) 