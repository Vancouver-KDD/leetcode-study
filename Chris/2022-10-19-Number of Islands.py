class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        numRows, numCols = len(grid), len(grid[0])
        
        visited = set()
        numIslands = 0
        
        
        
        def bfs(row, col):
            visited.add((row,col))
            q = collections.deque()
            q.append((row,col))
            
            
            while(q):
                r, c = q.pop()
                print(r,c)
                directions = [[r-1,c], [r+1,c],[r,c-1],[r,c+1]]
                
                for dr, dc in directions:
                    if dr >= 0 and dr < numRows and dc >= 0 and dc< numCols and grid[dr][dc] == "1" and (dr,dc) not in visited:
                        visited.add((dr,dc))
                        q.append((dr,dc))
                
                
                
        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    numIslands += 1
        
        
        return numIslands