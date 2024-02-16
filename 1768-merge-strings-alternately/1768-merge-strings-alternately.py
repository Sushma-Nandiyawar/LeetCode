class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final = ""
        w1 = len(word1)
        w2 = len(word2)
        i=0
        j=0
        while i<w1 or j<w2:
            if i<w1:
                final = final +word1[i]
                i += 1
            if j<w2:
                final = final + word2[j]
                j += 1
        return final