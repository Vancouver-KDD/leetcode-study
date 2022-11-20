class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        times = [[0] * cols] * rows
        
        for r in range(rows):
            for c in range(cols):
                print(grid[r][c] != 0)
                if grid[r][c] != 0:
                    times[r][c] = float("infinity")
                else:
                    times[r][c] = 0
        
        visited = set()
        
        def bfs(r, c, t):
            if r < 0 or r >= rows or c < 0 or c >= cols or times[r][c] == 0:
                return
            
            times[r][c] = min(times[r][c], t)
            
            if grid[r][c] == 1:
                bfs(r-1,c,t+1)
                bfs(r+1,c,t+1)
                bfs(r,c-1,t+1)
                bfs(r,c+1,t+1)
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    visited.clear()
                    bfs(r,c,0)
        
        maxTime = -1
        for r in range(rows):
            for c in range(cols):
                if times[r][c] == float("infinity"):
                    return -1
                maxTime = max( maxTime, times[r][c])
                    
        return maxTime