class Solution {
    /*
        Time Complexity: O(r * c)
        Space Complexity: O(1) in case where the whole grid is one big island
     */
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) return 0;

        int rows = grid.length;
        int cols = grid[0].length;
        int numOfIslands = 0;

        // visiting each cell in the grid

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (grid[i][j] == '1') {
                    numOfIslands++; // found a new island
                    dfs(grid, i, j); // makr entire island as visited
                }
            }
        }


        return numOfIslands;

    }

    private void dfs(char[][] grid, int i, int j) {
        int rows = grid.length;
        int cols = grid[0].length;

        // Base case: out of bounds or water or already visited
        if (i < 0 || i >= rows || j < 0 || j >= cols || grid[i][j] != '1') return;

        // Mark as visited
        grid[i][j] = '0';

        // Explore all 4 directions
        dfs(grid, i - 1, j); // up
        dfs(grid, i + 1, j); // down
        dfs(grid, i, j - 1); // left
        dfs(grid, i, j + 1); // right
    }
}