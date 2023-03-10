class Solution {
    static int count;
    public int numIslands(char[][] grid) {
        count = 0;
        for(int i = 0; i<grid.length;i++) {
            for(int j = 0;j<grid[0].length;j++) {
                if(grid[i][j] == '1') {
                    dfs(i, j, grid);
                    count++;
                }
            }
        }
        return count;
    }
    private void dfs(int i, int j, char[][] grid) {
        if(i>=grid.length || j>=grid[0].length || i<0 || j<0 || grid[i][j] !='1') {
            return;
        }

        grid[i][j] = '0';
        dfs(i+1, j, grid);
        dfs(i, j+1, grid);
        dfs(i-1, j, grid);
        dfs(i, j-1, grid);
    }
}
//time : O(cells) = O(M*N)