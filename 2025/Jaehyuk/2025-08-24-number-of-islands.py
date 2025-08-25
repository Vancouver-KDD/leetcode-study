class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        var:
            a) visited: a hashset that stores the coord visited ie) {(1,2), (3,4)} 
            b) numIslandDiscovered
        1. iterate through the grid, one coord at a time
        2. each time we check out a coord:
            a) ensure that we haven't visited this coord yet, if so, skip
            b) if its an ocean, mark it as visited and skip. Else, we increment numIslandDiscovered and start performing DFS below
            c) start perform DFS with the current coord as the root to visit all coord of current island. The DFS will attempt to visit all unvisited coord that is directly adjacent to current coord (horizational/vert). Each time a DFS visits a coord, we would mark it as visited. If the adjacent coord is an island, continue DFS. Else return
            d) once we exaust all coord of given island, we move on to next coord
        '''

        visited = set()
        numIslandDiscovered = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                data = grid[row][col]
                if (row,col) in visited:
                    continue
                if data == "0":
                    visited.add((row,col))
                else:
                    numIslandDiscovered += 1
                    self.dfs(row,col,visited,grid)

        return numIslandDiscovered


    def dfs(self,row,col,visited,grid):
        if row >= len(grid) or col >= len(grid[0]) or row < 0 or col < 0:
            return
        if (row,col) in visited:
            return

        visited.add((row,col))
        data = grid[row][col]

        if data == "0":
            return
        else:
            self.dfs(row+1, col, visited, grid)
            self.dfs(row, col+1, visited, grid)
            self.dfs(row-1, col, visited, grid)
            self.dfs(row, col-1, visited, grid)
        






                
                
                
        