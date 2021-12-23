class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        S = s.upper().replace('-', '')
        ls = len(S)
        if ls % k == 0:
            pos = k
        else:
            pos = ls % k
        res = S[:pos]
        while pos < ls:
            res += '-' + S[pos : pos + k]
            pos += k
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.licenseKeyFormatting("5F3Z-2e-9-w1", 4))