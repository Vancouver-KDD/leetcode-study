class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        row, col = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or r < 0 or c < 0 or r==row or c==col or heights[r][c] < prevHeight):
                return
            visit.add((r,c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])

        for c in range(col):
            dfs(0, c, pac, heights[0][c])
            dfs(row-1, c, atl, heights[row-1][c])

        for r in range(row):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, col-1, atl, heights[r][col -1])
        res = []
        for r in range(row):
            for c in range(col):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r,c])
        return res



                
                #check if each cell can reach both atlantic and pacific ocean
                # to check, check if left cell is less or equal to current cell and same to right cell
                # OR if atlantic ocean is on [1,0] to it or [0, -1]
                # ALSo check if pacific ocean is [-1,0] or [0,1] to it
