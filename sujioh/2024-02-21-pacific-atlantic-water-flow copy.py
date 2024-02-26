class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROW = len(heights)
        COL = len(heights[0])
        pac = set()
        atl = set()

        def dfs(r, c, visited, previousH):
            if (r<0 or c<0 or r>=ROW or c>=COL):
                return 
            if previousH > heights[r][c]:
                return 
            if (r,c) in visited:
                return 
            visited.add((r,c))
            dfs(r,c+1,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])
            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])

        for r in range(ROW):
            dfs(r,0,pac,0)
            dfs(r,COL-1,atl,0)
        for c in range(COL):
            dfs(0,c,pac,0)
            dfs(ROW-1,c,atl,0)
        return pac.intersection(atl)