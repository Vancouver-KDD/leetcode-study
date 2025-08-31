from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            stack = [(r, c)]
            while stack:
                x, y = stack.pop()
                if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                    grid[x][y] = '0'
                    stack.extend([(x+1,y),(x-1,y),(x,y+1),(x,y-1)])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        return count
