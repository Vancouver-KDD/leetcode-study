class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        for(int i = 0; i < grid.length; i++) {
            for(int j = 0; j < grid[0].length; j++) {
                if(grid[i][j] == '1') {
                    count++;
                    dfs(grid, i, j);
                }
            }
        }
        return count;
    }

    private void dfs(char[][] grid, int x, int y) {
        if((0 <= x && x < grid.length) && (0 <= y && y < grid[0].length) && grid[x][y] == '1') {
            grid[x][y] = '2';
            // right
            dfs(grid, x+1, y);
            // left
            dfs(grid, x-1, y);
            // up
            dfs(grid, x, y-1);
            // down
            dfs(grid, x, y+1);
        }

    }
}