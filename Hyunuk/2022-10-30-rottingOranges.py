import collections

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def is_valid(y, x):
            return 0 <= y < r and 0 <= x < c and grid[y][x] == 1
        
        r, c = len(grid), len(grid[0])
        q = collections.deque()
        ret = -1
        seen = set()
        fresh_cnt = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    q.append((i, j))
                    seen.add((i, j))
                elif grid[i][j] == 1:
                    fresh_cnt += 1
        while q:
            size = len(q)
            for _ in range(size):
                y, x = q.popleft()
                for dy, dx in directions:
                    curr_y, curr_x = y+dy, x+dx
                    curr = (y+dy, x+dx)
                    if curr not in seen and is_valid(curr_y, curr_x):
                        seen.add(curr)
                        q.append(curr)
                        grid[curr_y][curr_x] = 2
                        fresh_cnt -= 1
            ret += 1
        if fresh_cnt == 0:
            return ret if ret > -1 else 0
        return -1
