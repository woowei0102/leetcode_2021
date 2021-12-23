class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openList = ['[', '{', '(']
        closeList = [']', '}', ')']
        for i in s:
            if i in openList:
                stack.append(i)
            elif i in closeList:
                pos = closeList.index(i)
                if len(stack) > 0 and \
                    openList[pos] == stack[len(stack) - 1]:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True

if __name__ == '__main__':
    s = Solution()
    print(s.isValid(''))