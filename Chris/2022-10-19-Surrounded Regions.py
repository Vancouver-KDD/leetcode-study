class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        
        visited = set()
        
        
        
        def dfs(row, col):
            if row >= 0 and row < rows and col >= 0 and col < cols and board[row][col] == "O" and (row,col) not in visited:
                visited.add((row,col))
                dfs(row+1,col)
                dfs(row-1,col)
                dfs(row,col+1)
                dfs(row,col-1)
                board[row][col] = "E"
                
                
            
        
        
        for c in range(cols):
            dfs(0,c)
            dfs(rows-1,c)
        
        for r in range(rows):
            dfs(r,0)
            dfs(r,cols-1)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "E":
                    board[r][c] = "O"
                elif board[r][c] == "O":
                    board[r][c] = "X"