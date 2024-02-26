# https://leetcode.com/problems/max-area-of-island/
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        biggest = 0
        row, col = len(grid), len(grid[0])
        visited = [[False] * col for _ in range(row)]
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(x, y):
            queue = deque()
            queue.append((x, y))
            visited[x][y] = True
            areaNum = 1

            while queue:
                cur_x, cur_y = queue.popleft()
                for dx, dy in dirs:
                    next_x = cur_x + dx
                    next_y = cur_y + dy
                    if 0 <= next_x < row and 0 <= next_y < col:
                        if grid[next_x][next_y] == 1 and not visited[next_x][next_y]:
                            queue.append((next_x, next_y))
                            visited[next_x][next_y] = True
                            areaNum += 1
            return areaNum

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1 and not visited[i][j]:
                    biggest = max(biggest, bfs(i, j))

        return biggest
