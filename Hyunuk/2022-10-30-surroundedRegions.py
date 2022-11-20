class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def is_in_border(y, x):
            return y == 0 or x == 0 or y == r - 1 or x == c - 1
        
        def dfs(y, x):
            if 0 <= y < r and 0 <= x < c and board[y][x] == "O":
                board[y][x] = "E"
                for dy, dx in directions:
                    dfs(y+dy, x+dx)
                    
        """
        Do not return anything, modify board in-place instead.
        """
        r, c = len(board), len(board[0])
        directions = (0, 1), (0, -1), (1, 0), (-1, 0)
        for i in range(r):
            for j in range(c):
                if is_in_border(i, j) and board[i][j] == "O":
                    dfs(i, j)

        for i in range(r):
            for j in range(c):
                if board[i][j] == "E":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
