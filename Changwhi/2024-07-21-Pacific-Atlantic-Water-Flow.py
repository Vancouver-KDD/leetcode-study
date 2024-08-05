class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        if not heights or not heights[0]:
            return []
        
        max_row = len(heights)
        max_col = len(heights[0])
        pacificCheckVisiting = set()
        atlanticCheckVisiting = set()
        
        result = []
        def dfs(row, col, checkVisiting, prevCell):
            # Return if already visited, out of grid bounds, or if the height of the current cell
            # is smaller than the previous cell's height.
            if (row, col) in checkVisiting or row < 0 or col < 0 or row >= max_row or col >= max_col or heights[row][col] < prevCell:
                return
            
            # Mark this cell as visited.
            checkVisiting.add((row, col))
            
            # Continue traversing in all four directions.
            dfs(row + 1, col, checkVisiting, heights[row][col])
            dfs(row - 1, col, checkVisiting, heights[row][col])
            dfs(row, col + 1, checkVisiting, heights[row][col])
            dfs(row, col - 1, checkVisiting, heights[row][col])

        for row in range(max_row):
            # Check flows from the left and right edges.
            dfs(row, 0, pacificCheckVisiting, heights[row][0])
            dfs(row, max_col - 1, atlanticCheckVisiting, heights[row][max_col - 1])
            
        for col in range(max_col):
            # Check flows from the top and bottom edges.
            dfs(0, col, pacificCheckVisiting, heights[0][col])
            dfs(max_row - 1, col, atlanticCheckVisiting, heights[max_row - 1][col])            
            
        for row in range(max_row):
            for col in range(max_col):
                if (row, col) in pacificCheckVisiting and (row, col) in atlanticCheckVisiting:
                    result.append((row, col))
        return result
