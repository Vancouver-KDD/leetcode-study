class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        1. DFS through the graph with 4 directions
        2. Start from the top left, append pacific_water = (r, c) if you can traverse
        3. Do the same from the bottom right and see if the same coordinate exists in pacific_water
        4. if it does, add to results[2D]
        """
        rows, cols = len(heights), len(heights[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        pac = set()
        atl = set()
        def dfs(row, col, visited, prev_height):
            if (row, col) in visited or row < 0 or col < 0 or row >= rows or col >= cols or heights[row][col] < prev_height:
                return
            visited.add((row, col))
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
                dfs(new_row, new_col, visited, heights[row][col])


        for row in range(rows):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, cols - 1, atl, heights[row][cols-1])
        for col in range(cols):
            dfs(0, col, pac, heights[0][col])
            dfs(rows - 1, col, atl, heights[rows-1][col])

        results = []
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pac and (row, col) in atl:
                    results.append([row, col])
        return results

