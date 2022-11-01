class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:        
        # Check for an empty graph.
        if not heights:
            return []

        p_visited = set()
        a_visited = set()
        
        rows, cols = len(heights), len(heights[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))      
     
        def traverse(i, j, visited):
            if (i, j) in visited:
                return
            visited.add((i, j))
            # Traverse neighbors.
            for direction in directions:
                next_i, next_j = i + direction[0], j + direction[1]
                if 0 <= next_i < rows and 0 <= next_j < cols:
                    # Add in your question-specific checks.
                    if heights[next_i][next_j] >= heights[i][j]:
                        traverse(next_i, next_j, visited)

        for row in range(rows):
            traverse(row, 0, p_visited)
            traverse(row, cols - 1, a_visited)

        for col in range(cols):
            traverse(0, col, p_visited)
            traverse(rows - 1, col, a_visited)

        return list(p_visited & a_visited)