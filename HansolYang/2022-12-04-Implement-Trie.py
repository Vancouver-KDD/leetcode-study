class TrieNode:
    
    def __init__(self):
        self.words = dict()
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        
        for i in word:
            if i not in node.words:
                node.words[i] = TrieNode()
                
            node = node.words[i]
        
        node.is_end = True
    
    def _prefix_search(self, word):
        node = self.root
        for i in word:
            if i not in node.words:
                return False
            node = node.words[i]
        return node
    
    def search(self, word: str) -> bool:
        node = self._prefix_search(word)
        return node.is_end if node else False

    def startsWith(self, prefix: str) -> bool:
        node = self._prefix_search(prefix)
        return node


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)