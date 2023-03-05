class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        res = 0

        rows, cols, = len(grid), len(grid[0])

        def dfs(x, y):
            # Return on base case of out of bounds or we reach a "0"
            if x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] == "0":
                return

            # turn current cell to 0 and call DFS to make adjacent cells 0 through recursion
            if grid[x][y] == "1":
                grid[x][y] = "0"
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)

        # Performs DFS only when "1" is found and updates island counter,
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1

            # return answer
        return res