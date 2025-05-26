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

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        """
        Use Trie to keep track of the word
        DFS to traverse through the board and backtrack
        Add possible word in results
        """
        # Use Trie to keep track of the word
        root = TrieNode()
        for word in words:
            root.add_word(word)
        
        # Store visited and results
        visited = set()
        results = set()

        rows = len(board)
        cols = len(board[0])

        # DFS to traverse
        def dfs(r, c, node, word):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or board[r][c] not in node.children:
                return
        
            visited.add((r, c))
            # get to the next one
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.is_end:
                results.add(word)
            
            # Continue to find rest of the words
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            visited.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(results)
