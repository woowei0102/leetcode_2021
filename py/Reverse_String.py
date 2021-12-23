class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        ## method 1
        # return s[::-1]

        ## method 2
        # temp = []
        # for i in range(len(s)):
        #     temp.append(s.pop())
        # s = temp

        ## method 3
        i = 0
        j = len(s) - 1
        while (i < j):
            s[i], s[j] = s[j], s[i]#交換賦值
            i += 1
            j -= 1

if __name__ == '__main__':
    s = Solution()
    print(s.reverseString(["h","e","l","l","o"]))
        