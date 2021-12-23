class Solution:
    def wordPattern(self, pattern, str) -> bool:
        # method 1
        # if pattern is None or str is None:
        #     return True
        # # double map
        # words_to_pattern = {}
        # pattern_to_words = {}
        # word_list = str.split(' ')
        # if len(word_list) != len(pattern):
        #     return False
        # for index, word in enumerate(word_list):
        #     curr_p = pattern[index]
        #     if pattern_to_words.get(curr_p, word) != word or \
        #         words_to_pattern.get(word, curr_p) != curr_p:
        #         return False
        #     pattern_to_words[curr_p] = pattern_to_words.get(curr_p, word)
        #     words_to_pattern[word] = words_to_pattern.get(word, curr_p)
        # return True
        
        ## method 2
        s = {}
        t = {}
        word = str.split(' ')
        if len(word) != len(pattern):
            return False
        for i in range(len(pattern)):
            if s.get(pattern[i], word[i]) != word[i] or t.get(word[i], pattern[i]) != pattern[i]:
                return False
            s[pattern[i]] = word[i]
            t[word[i]] = pattern[i]
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.wordPattern('abba', 'dog cat cat fish'))
