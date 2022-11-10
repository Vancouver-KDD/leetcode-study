class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(y, x, pos, visited):
            if y < 0 or x < 0 or y >= r or x >= c or (y, x) in visited or board[y][x] != word[pos]:
                return False
            if pos == len(word) - 1:
                return True
            visited.add((y, x))
            for row, col in directions:    
                ret = dfs(y+row, x+col, pos+1, visited)
                if ret:
                    break
                    
            visited.remove((y, x))
            return ret
                
            
        if not board or not board[0]:
            return False
        if not word:
            return True
        
        r, c = len(board), len(board[0])
        ret = False
        visited = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for i in range(r):
            for j in range(c):
                if dfs(i, j, 0, visited):
                    return True
        return False
