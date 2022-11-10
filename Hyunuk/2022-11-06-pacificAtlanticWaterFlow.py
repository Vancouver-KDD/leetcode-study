class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def is_valid(y, x):
            return 0 <= y < r and 0 <= x < c
        
        def dfs(y, x, ocean):
            if (y, x) not in ocean:
                ocean.add((y, x))
                for dy, dx in directions:
                    if is_valid(y+dy, x+dx) and heights[y][x] <= heights[y+dy][x+dx]:
                        dfs(y+dy, x+dx, ocean)
            
        r, c = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(c):
            dfs(0, i, pacific)
            dfs(r-1, i, atlantic)
        for j in range(r):
            dfs(j, 0, pacific)
            dfs(j, c-1, atlantic)
        return list(pacific.intersection(atlantic))
