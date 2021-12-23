class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ## method 1
        # if len(s) != len(t):
        #     return False
        # ls = len(s)
        # mapStoT = [0] * 127
        # mapTtoS = [0] * 127
        # for i in range(ls):
        #     s_num, t_num = ord(s[i]), ord(t[i])
        #     if mapStoT[s_num] == 0 and mapTtoS[t_num] == 0:
        #         mapStoT[s_num] = t_num
        #         mapTtoS[t_num] = s_num
        #     elif mapTtoS[t_num] != s_num or mapStoT[s_num] != t_num:
        #         return False
        # return True

        ## method 2
        return [s.find(i) for i in s] == [t.find(j) for j in t]
        
if __name__ == '__main__':
    s = Solution()
    print(s.isIsomorphic('add', 'egg'))