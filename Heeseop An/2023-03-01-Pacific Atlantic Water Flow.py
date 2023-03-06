class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        visitedFromPacific = set()
        visitedFromAtlantic = set()

        def dfs(r, c, visited, prevHeight):
            if (r, c) in visited or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prevHeight:
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(cols):
            dfs(0, c, visitedFromPacific, heights[0][c])
            dfs(rows - 1, c, visitedFromAtlantic, heights[rows - 1][c])

        for r in range(rows):
            dfs(r, 0, visitedFromPacific, heights[r][0])
            dfs(r, cols - 1, visitedFromAtlantic, heights[r][cols - 1])

        result = []

        for c in range(cols):
            for r in range(rows):
                if (r, c) in visitedFromAtlantic and (r, c) in visitedFromPacific:
                    result.append([r, c])

        return result
