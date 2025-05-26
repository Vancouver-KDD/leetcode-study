class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = None


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def createTrie(self, words):
        for word in words:
            curr_node = self.root
            for letter in word:
                if letter not in curr_node.children:
                    curr_node.children[letter] = TrieNode()
                curr_node = curr_node.children[letter]
            curr_node.end = word

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = set()
        self.createTrie(words)

        def dfs(row, col, node, seen):
            if node.end:
                res.add(node.end)
                node.end = None

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols and (new_row, new_col) not in seen and board[new_row][
                    new_col] in node.children:
                    seen.add((new_row, new_col))
                    dfs(new_row, new_col, node.children[board[new_row][new_col]], seen)
                    seen.remove((new_row, new_col))

            # Prune the trie node if it is no longer needed
            if not node.children:
                del node

        for row in range(rows):
            for col in range(cols):
                if board[row][col] in self.root.children:
                    dfs(row, col, self.root.children[board[row][col]], {(row, col)})

        return list(res)