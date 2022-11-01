class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # bfs, set
        if not grid or not grid[0]:
            return 0
        r = len(grid)
        c = len(grid[0])
        ret = 0
        seen = set()
        q = deque()
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1" and (i, j) not in seen:
                    ret += 1
                    seen.add((i, j))
                    q.append((i, j))
                    while q:
                        curr = q.pop()
                        if is_valid(curr):
                            seen.add(curr)
        return ret
        