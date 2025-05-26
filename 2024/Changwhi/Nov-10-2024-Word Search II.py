class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
            # Step 1: Build the Trie
        trie = Trie()
        for word in words:
            trie.insert(word)

        rows, cols = len(board), len(board[0])
        result = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

        def backtrack(row, col, parent):
            char = board[row][col]
            node = parent.children[char]

            # Check if we found a word
            if node.is_end_of_word:
                result.add(node.word)

            # Mark the cell as visited by replacing it with '#'
            board[row][col] = '#'

            # Explore neighbors in 4 directions
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < rows and 0 <= new_col < cols and board[new_row][new_col] in node.children:
                    backtrack(new_row, new_col, node)

            # Restore the cell after backtracking
            board[row][col] = char

            # Optimization: Remove the leaf node if it's not needed anymore
            if not node.children:
                parent.children.pop(char)

        # Step 2: Start backtracking from each cell on the board
        for row in range(rows):
            for col in range(cols):
                if board[row][col] in trie.root.children:
                    backtrack(row, col, trie.root)

        return list(result)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word = None  # Store the complete word at the end node

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.word = word  # Mark the end node with the word
