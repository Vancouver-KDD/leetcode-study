from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, ocean):
            ocean.add((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and
                    (nr, nc) not in ocean and heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, ocean)

        pacific_reachable = set()
        atlantic_reachable = set()

        for r in range(rows):
            dfs(r, 0, pacific_reachable)
            dfs(r, cols - 1, atlantic_reachable)

        for c in range(cols):
            dfs(0, c, pacific_reachable)
            dfs(rows - 1, c, atlantic_reachable)

        result = list(pacific_reachable & atlantic_reachable)
        return result

solution = Solution()
example1 = [
  [4, 2, 7, 3, 4],
  [7, 4, 6, 4, 7],
  [6, 3, 5, 3, 6]
]
example2 = [[1], [1]]

output1 = solution.pacificAtlantic(example1)
output2 = solution.pacificAtlantic(example2)
print(output1)
print(output2)
