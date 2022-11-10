from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, at1 = set(), set()
        def dfs(r, c, visit, prevHeight):
            if((r,c) in visit or r<0 or c<0 or r==ROWS or c ==COLS or hieghts[r][c] < prevHeight):
                return
            visit.add((r,c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, c, visit, heights[r][c])
            dfs(r, c-1, c, visit, heights[r][c])
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS -1, c, at1, heights[ROWS-1][c])
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][c])
            dfs(r, COLS-1, at1, heights[r][c])
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if(r,c) in pac and (r,c) in at1:
                    res.append([r,c])
        return res

