class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # letter_map = {}
        # for letter in magazine:
        #     letter_map[letter] = letter_map.get(letter, 0) + 1
        # for letter in ransomNote:
        #     letter_map[letter] = letter_map.get(letter, 0) - 1
        #     if letter_map[letter] < 0:
        #         return False
        # return True

        for c in set(ransomNote):
            if ransomNote.count(c) > magazine.count(c):
                return False            
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canConstruct('a', 'ab'))
