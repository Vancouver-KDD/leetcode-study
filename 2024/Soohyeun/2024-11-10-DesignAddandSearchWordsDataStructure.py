class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                curr_node.children[letter] = TrieNode()
            curr_node = curr_node.children[letter]
        curr_node.end = True

    def searchHelper(self, word: str, curr_root: TrieNode):
        curr_node = curr_root
        for index, letter in enumerate(word):
            if letter == ".":
                if index + 1 == len(word):
                    for child in curr_node.children.values():
                        if child.end:
                            return True
                    return False
                for child in curr_node.children.values():
                    if self.searchHelper(word[index + 1:], child):
                        return True
                return False
            else:
                if letter not in curr_node.children:
                    return False
                curr_node = curr_node.children[letter]
        return curr_node.end

    def search(self, word: str) -> bool:
        return self.searchHelper(word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)