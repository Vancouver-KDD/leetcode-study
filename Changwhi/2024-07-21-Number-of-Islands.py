class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #bfs
        
        if not grid:
            return 0
        
        #create grid
        ROWS, COLS = len(grid), len(grid[0])
        #create visit list
        visit = set()
        
        def bfs(r,c):
            queue = []
            visit.add((r,c))
            queue.append((r,c))
            
            while queue:
                currentRow, currentCol = queue.pop(0)
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                
                for dr, dc in directions:
                    r = dr + currentRow
                    c = dc + currentCol
                    if (0 <= r < ROWS and
                        0 <= c < COLS and
                        grid[r][c] == '1' and
                        (r,c) not in visit
                       ):
                        queue.append((r,c))
                        visit.add((r,c))        
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visit and grid[r][c] == '1':
                    bfs(r,c)
                    res += 1
        return res