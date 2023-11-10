def exist(board, word):
    def backtrack(row, col, index):
        if index == len(word):
            return True

        if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != word[index]:
            return False

        temp = board[row][col]
        board[row][col] = "#"

        found = (backtrack(row + 1, col, index + 1) or
                 backtrack(row - 1, col, index + 1) or
                 backtrack(row, col + 1, index + 1) or
                 backtrack(row, col - 1, index + 1))

        board[row][col] = temp

        return found

    m, n = len(board), len(board[0])

    for i in range(m):
        for j in range(n):
            if backtrack(i, j, 0):
                return True

    return False

# Test case
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(exist(board, word))  # Output: true
