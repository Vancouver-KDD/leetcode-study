class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.cache = set()
        self.len = 0

    def addWord(self, word: str) -> None:
        self.cache.add(word)
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True
        self.len = max(self.len, len(word))

    def search(self, word: str) -> bool:
        def _search_helper(node, word):
            for i in range(len(word)):
                if word[i] == ".":
                    for j in node.children:
                        if _search_helper(node.children[j], word[i+1:]):
                            return True
                if word[i] not in node.children:
                    return False
                node = node.children[word[i]]
            return node and node.is_end
        
        if len(word) > self.len:
            return False
        ret = False
        if _search_helper(self.root, word):
            self.cache.add(word)
            ret = True
        return word in self.cache or ret


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
