class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(y, x):
            if 0 <= y < r and 0 <= x < c and grid[y][x] == 1:
                grid[y][x] = 0
                return 1 + dfs(y+1, x) + dfs(y-1, x) + dfs(y, x-1) + dfs(y, x+1)
            return 0
                
                
        ret = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                temp = 0
                if grid[i][j] == 1:
                    temp = dfs(i, j)
                ret = max(ret, temp)
        return ret
