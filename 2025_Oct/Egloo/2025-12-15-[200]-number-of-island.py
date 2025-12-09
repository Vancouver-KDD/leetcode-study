class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        x = len(grid[0])
        y = len(grid)

        visited = [[0 for _ in range(x)] for _ in range(y)]

        def visit(i, j):
            if i >= y or i < 0 or j >= x or j < 0:
                return 
            if visited[i][j] == 1 or grid[i][j] == "0":
                return 

            visited[i][j] = 1

            visit(i+1, j)
            visit(i-1, j)
            visit(i, j+1)
            visit(i, j-1)
            
        count = 0
        for i in range(y):
            for j in range(x):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    count += 1
                    visit(i,j)

        return count