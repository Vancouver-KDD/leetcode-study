class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        total_fresh = 0
        rotten = deque([])
        
        for y in range(m):
            for x in range(n):
                if grid[y][x] == 1:
                    total_fresh += 1
                if grid[y][x] == 2:
                    rotten.append((y,x))
                    
        while rotten and total_fresh > 0:
            minutes_passed += 1
            
            for _ in range
        