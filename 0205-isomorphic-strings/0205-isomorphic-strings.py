class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        compare = {}
        
        for i,j in zip(s,t):
            if i in compare:
                if compare[i] != j:
                    return False
            elif j in compare.values():
                return False
            compare[i] = j
        return True