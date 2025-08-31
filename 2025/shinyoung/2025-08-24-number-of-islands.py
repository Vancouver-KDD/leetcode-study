class Solution:
    def numIslands(self, grid):
        # T: O(m * n)
        # S: O(m * n)

        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            else:
                grid[i][j] = '0'
                dfs(i, j + 1)  # right
                dfs(i + 1, j)  # down
                dfs(i, j - 1)  # left
                dfs(i - 1, j)  # up

        number_of_islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    number_of_islands += 1
                    dfs(i, j)

        return number_of_islands


solution = Solution()
print(solution.numIslands(grid=[
  ["1", "1", "1", "1", "0"],
  ["1", "1", "0", "1", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "0", "0", "0"]
]))
print(solution.numIslands(grid=[
  ["1", "1", "0", "0", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "0", "0", "1", "1"]
]))
