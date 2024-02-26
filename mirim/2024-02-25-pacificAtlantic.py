# https://leetcode.com/problems/pacific-atlantic-water-flow/
from collections import deque


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        pacificVisited = set()
        atlanticVisited = set()
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(x, y, visited):
            visited.add((x, y))
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x < row and 0 <= new_y < col:
                    higher = heights[new_x][new_y] >= heights[x][y]
                    if (new_x, new_y) not in visited and higher:
                        dfs(new_x, new_y, visited)

        for i in range(row):
            dfs(i, 0, pacificVisited)
            dfs(i, col - 1, atlanticVisited)

        for j in range(col):
            dfs(0, j, pacificVisited)
            dfs(row - 1, j, atlanticVisited)

        return list(pacificVisited.intersection(atlanticVisited))
