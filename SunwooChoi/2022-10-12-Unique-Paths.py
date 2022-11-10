class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # create m x n list
        path_sum = [[0] * n for _ in range(m)]
        
        # set outside path sum to 1
        for col in range(n):
            path_sum[0][col] = 1
        for row in range(m):
            path_sum[row][0] = 1
            
        for row in range(1, m):
            for col in range(1, n):
                path_sum[row][col] = path_sum[row][col-1] + path_sum[row-1][col]
        
        return path_sum[-1][-1]
