class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        numRows = len(heights)
        numCols = len(heights[0])
        
        # visited set for pacific and atlantic 
        pac, atl = set(), set()
        
        
        def dfs(r, c, visited, prevHeight):
            
            if r<0 or c<0 or r == numRows or c == numCols or (r,c) in visited or prevHeight > heights[r][c]:
                return
            
            visited.add((r,c))
            
            dfs(r-1,c, visited, heights[r][c])
            dfs(r+1,c, visited, heights[r][c])
            dfs(r,c-1, visited, heights[r][c])
            dfs(r,c+1, visited, heights[r][c])
            
            return
        
        
        for c in range(numCols):
            dfs(0,c,pac, heights[0][c])
            dfs(numRows-1,c,atl, heights[numRows-1][c])
        
        for r in range(numRows):
            dfs(r,0,pac, heights[r][0])
            dfs(r,numCols-1,atl, heights[r][numCols-1])
        
        res = []
        
        for c in range(numCols):
            for r in range(numRows):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
                    
        return res
                    
        
