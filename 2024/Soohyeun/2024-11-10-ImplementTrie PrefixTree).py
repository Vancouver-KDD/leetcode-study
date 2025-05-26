class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_node = False


class Trie:
    def __init__(self):
        self.root_node = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root_node
        for letter in word:
            if letter not in curr_node.children:
                curr_node.children[letter] = TrieNode()
            curr_node = curr_node.children[letter]
        curr_node.end_node = True

    def search(self, word: str) -> bool:
        curr_node = self.root_node
        for letter in word:
            if letter not in curr_node.children:
                return False
            curr_node = curr_node.children[letter]
        return curr_node.end_node

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root_node
        for letter in prefix:
            if letter not in curr_node.children:
                return False
            curr_node = curr_node.children[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)2