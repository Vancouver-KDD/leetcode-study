class Trie:

    def __init__(self):
        self.prefix = {}

    def insert(self, word: str) -> None:
        pos = self.prefix
        for c in word:
            if c not in pos:
                pos[c] = {}                
            pos = pos[c]
        # marker to store word
        pos[""] = True

    def search(self, word: str) -> bool:
        pos = self.getPos(word)
        if not pos:
            return False
        
        return "" in pos

    def startsWith(self, prefix: str) -> bool:        
        return self.getPos(prefix) is not None
    
    # get dictionary of word
    def getPos(self, word: str):
        pos = self.prefix
        for c in word:
            if c not in pos:
                return None
            else:
                pos = pos[c]
        return pos

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

