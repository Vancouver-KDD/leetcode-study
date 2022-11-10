class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        
        def dfs(i, j):
            if i == len(grid) or j == len(grid[0]) or i == -1 or j == -1:
                return
            if grid[i][j] == "0":
                return

            
            grid[i][j] = "0"
            
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    counter += 1
                    dfs(i,j)
                    
        return counter