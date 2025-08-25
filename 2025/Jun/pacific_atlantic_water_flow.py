class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row_len = len(heights)
        col_len = len(heights[0])
        pacific = set()
        atlantic = set()
        def dfs(visited, row, col, prev_height):
            if 0 <= row < row_len and 0 <= col < col_len and heights[row][col] >= prev_height and (row, col) not in visited:
                visited.add((row, col))
                current_height = heights[row][col]
                dfs(visited, row+1, col, current_height)
                dfs(visited, row-1, col, current_height)
                dfs(visited, row, col+1, current_height)
                dfs(visited, row, col-1, current_height)

        res = []
        for i in range(row_len):
            dfs(pacific, i, 0, heights[i][0])
            dfs(atlantic, i, col_len - 1, heights[i][col_len - 1])

        for i in range(col_len):
            dfs(pacific, 0, i, heights[0][i])
            dfs(atlantic, row_len - 1, i, heights[row_len - 1][i])

        for (r,c) in pacific & atlantic:
            res.append([r,c])

        return res

