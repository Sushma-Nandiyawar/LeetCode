class TrieNode:
    def __init__(self):
        self.childeren = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode() 

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.childeren:
                cur.childeren[c] = TrieNode()
            cur = cur.childeren[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        
        def dfs(j,root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if word[i] == ".":
                    for child in cur.childeren.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in cur.childeren:
                        return False
                    cur = cur.childeren[c]
            return cur.endOfWord
        return dfs(0, self.root)


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)