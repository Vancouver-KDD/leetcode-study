"""
230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed)
 of all the values of the nodes in the tree.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.is_word
            if word[i] == '.':
                for child in node.children.values():
                    if dfs(child, i+1):
                        return True
            else:
                if word[i] in node.children:
                    if dfs(node.children[word[i]], i+1):
                        return True
            return False

        return dfs(self.root, 0)


def main():
    pass


if __name__ == "__main__":
    main()
