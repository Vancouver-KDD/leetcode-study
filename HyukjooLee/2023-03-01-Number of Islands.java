// Given an m x n 2D binary grid grid which represents
// a map of '1's (land) and '0's (water), return the number of islands.

// An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
// You may assume all four edges of the grid are all surrounded by water.


// using DFS, start from the top-left corner of the grid and iterate through each cell
// if a cell contains '1' and has not been visited before,
// we recursively visit its neighboring cells 
// time complexity of this algorithm is O(mn) as we visit each cell at most once
// the space complexity is also O(MN) as we use recursion to traverse the grid.
public class Solution {
    public int numIslands(char[][] grid) {
        // check if the grid is valid or not
        if (grid == null || grid.length == 0 || grid[0].length == 0) {
            return 0;
        }
        
        int numRows = grid.length;
        int numCols = grid[0].length;
        int numIslands = 0;
        
        // traverse each cell in the grid
        for (int row = 0; row < numRows; row++) {
            for (int col = 0; col < numCols; col++) {
                // if the cell is a part of unvisited island, mark and continue its cells nearby
                if (grid[row][col] == '1') {
                    numIslands++;
                    markIslandAsVisited(grid, row, col);
                }
            }
        }
        
        return numIslands;
    }
    
    // mark the current island as visited 
    private void markIslandAsVisited(char[][] grid, int row, int col) {
        if (row < 0 || row >= grid.length || col < 0 || col >= grid[0].length || grid[row][col] == '0') {
            return;
        }
        
        grid[row][col] = '0';
        markIslandAsVisited(grid, row - 1, col);
        markIslandAsVisited(grid, row + 1, col);
        markIslandAsVisited(grid, row, col - 1);
        markIslandAsVisited(grid, row, col + 1);
    }
}
