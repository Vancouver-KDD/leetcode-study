class TrieNode:
    def __init__(self):
        self.words = dict()
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for i in word:
            if i not in node.words:
                node.words[i] = TrieNode()
            node = node.words[i]
            
        node.is_end = True

    def search(self, word: str) -> bool:
        
        node = self.root
        
        def dfs(i: int, n):
            
            if i == len(word):
                return n
            
            if word[i] == ".":
                for j in n.words.keys():
                    ret = dfs(i+1, n.words[j])
                    if ret and ret.is_end:
                        return ret
                return False
            else:
                if word[i] in n.words:
                    return dfs(i+1, n.words[word[i]])
                else:
                    return False
        
        res = dfs(0, node)
        
        return res if not res else res.is_end
            
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)