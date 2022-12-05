class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        visit = set()
        dp = [[1] * col for _ in range(row)]
        res = 0
        
        moves = ((0,1),(0,-1),(1,0),(-1,0))
        
        def inside_border(i,j):
            return (0 <= i < row) and ( 0 <= j < col)
        
        
        def dfs(i, j):
            if not inside_border(i,j) or (i,j) in visit:
                return
            visit.add((i,j))
            
            #recursively mark dp
            for dx, dy in moves:
                x = i + dx
                y = j + dy
                if inside_border(x,y) and matrix[x][y] > matrix[i][j]:
                    dfs(x,y)
                    dp[i][j] = max(dp[x][y] + 1, dp[i][j])
            
            nonlocal res
            res = max(dp[i][j], res)

            
        for i in range(row):
            for j in range(col):
                dfs(i,j)
                
        # return max from dp
        return res
        