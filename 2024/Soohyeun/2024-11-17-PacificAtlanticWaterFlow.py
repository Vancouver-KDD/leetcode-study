class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific = {(0, 0)}
        atlantic = {(m-1, n-1)}

        def dfs(row, col, visited, ocean):
            nonlocal m, n
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if new_row < 0 or new_col < 0 or new_row >= m or new_col >= n or (new_row, new_col) in visited:
                    continue
                if (ocean == "pacific" and (new_row == 0 or new_col == 0)) \
                        or (ocean == "atlantic" and (new_row == m-1 or new_col == n-1)) \
                        or heights[row][col] <= heights[new_row][new_col]:
                    visited.add((new_row, new_col))
                    dfs(new_row, new_col, visited, ocean)

        dfs(0, 0, pacific, "pacific")
        dfs(m-1, n-1, atlantic, "atlantic")

        res = [[row, col] for row, col in pacific if (row, col) in atlantic]
        return res
