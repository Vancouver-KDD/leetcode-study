class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, word, row, col, visit):
            if len(word) == 0:
                return True
            elif len(word) == 1:
                return board[row][col] == word 
            else:
                if board[row][col] == word[0]:
                    visit[row][col] = True
                    if row > 0 and not visit[row-1][col]:
                        if dfs(board, word[1:], row-1, col, visit):
                            return True
                    if row < height-1 and not visit[row+1][col]:
                        if dfs(board, word[1:], row+1, col, visit):
                            return True
                    if row > 0 and not visit[row][col-1]:
                        if dfs(board, word[1:], row, col-1, visit):
                            return True
                    if row < width-1 and not visit[row][col+1]:
                        if dfs(board, word[1:], row, col+1, visit):
                            return True
                    visit[row][col] = False
                    return False
                else:
                    return False
                
        height = len(board)
        width = len(board[0])
        
        # extra 2d list for marking visit
        visit = [[False]*width for _ in range(height)]
        
        if height == 1 and width == 0:
            return len(word) == 0
        
        for i in range(height):
            for j in range(width):
                if dfs(board, word, i, j, visit):
                    return True
        return False

