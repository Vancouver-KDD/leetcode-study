class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        dp = [[0]*COL for _ in range(ROW)]
        dp[0][0] = grid[0][0]

        for i in range(ROW):
            for j in range(COL):
                if i == 0 and j == 0:
                    continue
                top = dp[i-1][j] if i-1 >= 0 else float('inf')
                left = dp[i][j-1] if j-1 >= 0 else float('inf')
                min_prev = min(top, left)
                dp[i][j] = min_prev + grid[i][j]
        return dp[ROW-1][COL-1]