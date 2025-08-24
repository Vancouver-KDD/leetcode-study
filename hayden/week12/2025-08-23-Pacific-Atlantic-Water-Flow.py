from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])
        def bfs(starts):
            vis = [[False]*n for _ in range(m)]
            q = deque(starts)
            for r, c in starts:
                vis[r][c] = True
            while q:
                r, c = q.popleft()
                for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < m and 0 <= nc < n and not vis[nr][nc] and heights[nr][nc] >= heights[r][c]:
                        vis[nr][nc] = True
                        q.append((nr, nc))
            return vis
        pac = [(0, j) for j in range(n)] + [(i, 0) for i in range(m)]
        atl = [(m-1, j) for j in range(n)] + [(i, n-1) for i in range(m)]
        vp = bfs(pac)
        va = bfs(atl)
        res = []
        for i in range(m):
            for j in range(n):
                if vp[i][j] and va[i][j]:
                    res.append([i, j])
        return res
