class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        numRows = len(heights)
        numCols = len(heights[0])
        
        pac, atl = set(), set()
        
        
        def dfs(r,c, visited, prevHeight):
            if( (r,c) in visited or r<0 or c<0 or r== numRows or c==numCols or heights[r][c] < prevHeight):
                return
            
            visited.add((r,c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
            
        
        
        for c in range(numCols):
            dfs(0, c, pac, heights[0][c])
            dfs(numRows - 1, c, atl, heights[numRows - 1][c])
            
        
        for r in range(numRows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, numCols-1, atl, heights[r][numCols -1])
            
        
        res = []
        
        for r in range(numRows):
            for c in range(numCols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r,c])
                    
        return res