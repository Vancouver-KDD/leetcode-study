class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.memo = {}

    def createTrie(self, wordDict: list[str]):
        for word in wordDict:
            curr_node = self.root
            for letter in word:
                if letter not in curr_node.children:
                    curr_node.children[letter] = TrieNode()
                curr_node = curr_node.children[letter]
            curr_node.end = True

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        self.createTrie(wordDict)

        def findwords(index):
            if index in self.memo:
                return self.memo[index]
            curr_node = self.root
            while index < len(s):
                if s[index] in curr_node.children:
                    curr_node = curr_node.children[s[index]]
                else:
                    self.memo[index] = False
                    return False
                index += 1
                if curr_node.end and findwords(index):
                    self.memo[index] = True
                    return True
            self.memo[index] = curr_node.end
            return curr_node.end

        return findwords(0)
