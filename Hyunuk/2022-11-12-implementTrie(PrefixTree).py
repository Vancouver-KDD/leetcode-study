class TrieNode:
    
    def __init__(self):
        self.children = dict()
        self.end_of_word = False
        
    
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def _search_prefix(self, word):
        node = self.root
        for c in word:
            if not node.children.get(c):
                return False
            node = node.children[c]
        return node
    
    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.end_of_word = True

    def search(self, word: str) -> bool:
        node = self._search_prefix(word)
        return node and node.end_of_word

    def startsWith(self, prefix: str) -> bool:
        return self._search_prefix(prefix)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
