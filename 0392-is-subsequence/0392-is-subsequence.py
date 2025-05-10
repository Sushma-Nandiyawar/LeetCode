class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c = 0
        if len(s) == 0:
            return True
        for i in t:
            if i==s[c]:
                c += 1
            if c ==len(s):
                break
        return c==len(s)
