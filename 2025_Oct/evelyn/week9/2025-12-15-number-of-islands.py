from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        cnt = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cnt+=1
                    self.bfs(grid, i, j)

        return cnt

    def bfs(self, grid, x, y):
        q = deque()
        q.append((x, y))
        grid[x][y] = "2"

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        while q:
            curX, curY = q.popleft()

            for i in range(4):
                newX = curX + dx[i]
                newY = curY + dy[i]

                if newX >= 0 and newX < len(grid) and newY >= 0 and newY < len(grid[0]) and grid[newX][newY] == "1":
                    grid[newX][newY] = "2"
                    q.append((newX, newY))