class Solution {
    public int numIslands(char[][] grid) {
        int count = 0;
        for(int i =0 ; i<grid.length; i++) {
            for(int j = 0; j<grid[i].length; j++) {
                if(grid[i][j] == '1') {
                    count++;
                    bfs(grid, i, j);
                }
            }
        }
        return count;
    }
    
    private void bfs(char[][] grid, int i, int j) {
        if(i<0 || i>=grid.length || j<0 || j>=grid[i].length|| grid[i][j] == '0') return;
        grid[i][j] = '0';
        bfs(grid, i+1, j); //check up
        bfs(grid, i-1, j); //check down
        bfs(grid, i, j-1); //check left
        bfs(grid, i, j+1); //check right  
    }
}