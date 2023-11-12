class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def dfs(row, col, curr_len):
            if row < 0 or len(board) <= row or col < 0 or len(board[0]) <= col:
                return False

            curr_word = word[len(word) - curr_len]

            if board[row][col] != curr_word:
                return False

            if curr_len == 1:
                return True

            prev = board[row][col]

            board[row][col] = None

            top = dfs(row - 1, col, curr_len - 1)
            down = dfs(row + 1, col, curr_len - 1)
            left = dfs(row, col - 1, curr_len - 1)
            right = dfs(row, col + 1, curr_len - 1)

            board[row][col] = prev

            return top or down or left or right

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, len(word)):
                    return True

        return False