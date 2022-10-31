import collections

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        def is_valid(y, x, m):
            return 0 <= y < r and 0 <= x < c and rooms[y][x] > m + 1
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2 ** 31 - 1
        r, c = len(rooms), len(rooms[0])
        q = collections.deque()
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for i in range(r):
            for j in range(c):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))
        while q:
            y, x, m = q.popleft()
            for dy, dx in directions:
                if is_valid(y+dy, x+dx, m):
                    rooms[y+dy][x+dx] = m+1
                    q.append((y+dy, x+dx, m+1))
