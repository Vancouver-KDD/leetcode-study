class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        row = len(grid)
        col = len(grid[0])
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    count += 1
                    self.DFS(grid, i, j)
        
        return count
                    
        
    def DFS(self, graph, i, j):
        if i < 0 or i >= len(graph) or j < 0 or j >= len(graph[0]) or graph[i][j] != 1:
            return
 
        # mark it as visited
        graph[i][j] = '0'
 
        # Recur for 8 neighbours
        self.DFS(i - 1, j - 1)
        self.DFS(i - 1, j)
        self.DFS(i - 1, j + 1)
        self.DFS(i, j - 1)
        self.DFS(i, j + 1)
        self.DFS(i + 1, j - 1)
        self.DFS(i + 1, j)
        self.DFS(i + 1, j + 1)