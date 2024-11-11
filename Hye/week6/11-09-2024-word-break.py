class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def add_word(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word):
        # return the length of the word
        curr = self
        i = 1
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
            if curr.is_end:
                return i
            i += 1
        return False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Initialize Trie with words
        root = TrieNode()
        for word in wordDict:
            root.add_word(word)
 
        # Iterate through the string and check for words each word should return is_end == True
        index = 0
        while index < len(s):
            print("index: ", index)
            next_index = root.search(s[index:])
            if next_index is False:
                return False
            index += next_index
        return True
