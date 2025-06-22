# Design Word Search Data Structure

class TrieNode():
    def __init__(self):
        self.children = dict()
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True
        
    def search(self, word: str) -> bool:

        def dfs(j, curr):
            for i in range(j, len(word)):
                c = word[i]
                
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.is_end
        

        return dfs(0, self.root)
