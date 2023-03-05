"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""
class Solution:
    def numIslands(self, grid) -> int:
        # use DFS
        rows, cols = len(grid), len(grid[0])
        visited = [ [0]* cols for _ in range(rows)]
        num_island = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and not visited[r][c]:
                    self.dfs(grid, r, c, visited)
                    num_island += 1
        return num_island


    def dfs(self, grid, r, c, visited):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]) or visited[r][c] == 1:
            return
        # propagate only if it is island
        if grid[r][c] == "1":
            visited[r][c] = 1
            self.dfs(grid, r+1, c, visited)
            self.dfs(grid, r-1, c, visited)
            self.dfs(grid, r, c+1, visited)
            self.dfs(grid, r, c-1, visited)

