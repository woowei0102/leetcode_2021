class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        :type s: str
        :rtype: str
        """
        # str_index = []
        # vowel = []
        # res = []
        # pos = -1
        # for index, value in enumerate(s):
        #     if value in 'aeiouAEIOU':
        #         str_index.append(-1)
        #         vowel.append(value)
        #     else:
        #         str_index.append(index)
        # for index in str_index:
        #     if index < 0:
        #         res.append(vowel[pos])
        #         pos -= 1
        #     else:
        #         res.append(s[index])
        # return "".join(res)

        index = []
        vowel = []
        res = []
        pos = -1
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                index.append(-1)
                vowel.append(s[i])
            else:
                index.append(s[i])
        for i in range(len(index)):
            if index[i] == -1:
                res.append(vowel[pos])
                pos -= 1
            else:
                res.append(s[i])
        return "".join(res)
        

if __name__ == '__main__':
    s = Solution()
    print(s.reverseVowels("hello"))