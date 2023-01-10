class WordDictionary:

    def __init__(self):
        self.prefix = {}
        self.isEnd = False
    def addWord(self, word: str) -> None:
        pos = self.prefix
        for c in word:
            if c not in pos:
                pos[c] = {}                
            pos = pos[c]
        # marker to store word
        pos[""] = True
        
    def search(self, word: str) -> bool:
        return self.searchPrefix(self.prefix, word, 0)
        
    # get dictionary of word
    def searchPrefix(self, pos, word, idx):
        if len(word) == idx:
            if "" in pos:
                return True
            return False
        if word[idx] == ".":
            for key in pos:
                if key != "":
                    if self.searchPrefix(pos[key], word, idx+1):
                        return True
            return False
        if word[idx] != ".":
            if word[idx] not in pos:
                return False
            return self.searchPrefix(pos[word[idx]], word, idx+1)
        
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

