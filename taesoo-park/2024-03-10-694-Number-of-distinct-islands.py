class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(x, y, direction):
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return
            grid[x][y] = 0  # Mark as visited
            path.append(direction)  # Record the direction of movement
            # Explore all four directions
            dfs(x + 1, y, 'D')  # Down
            dfs(x - 1, y, 'U')  # Up
            dfs(x, y + 1, 'R')  # Right
            dfs(x, y - 1, 'L')  # Left
            path.append('B')  # Backtrack marker

        distinctIslands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:  # Start of a new island
                    path = []
                    dfs(i, j, 'S')  # 'S' as start
                    distinctIslands.add(tuple(path))  # Add the path tuple to the set
        
        return len(distinctIslands)
