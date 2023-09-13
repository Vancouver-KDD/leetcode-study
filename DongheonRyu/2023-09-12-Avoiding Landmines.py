

grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

# Recurrence relation
# grid[n-1][m-1] = grid[n-1][m] + grid[n][m-1]
# 
# 1 1 1
# 1 0 1
# 1 1 1

grid = [[1,1,1],[1,0,1],[1,1,1]]
def findTheWay(grid):
    n = len(grid)
    m = len(grid[0])
    mod = (10**9)+7

    dp = [[0]* m for _ in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                if i>0:
                    dp[i][j] += dp[i-1][j]
                if j>0:
                    dp[i][j] += dp[i][j-1]    
    
    return dp[n-1][m-1] % mod


print(findTheWay(grid))