class Solution {
    public int numIslands(final char[][] grid) {       
    int count = 0;
    for (int i=0;i<grid.length;i++)
        for (int j=0;j<grid[0].length;j++)
            if (paint(grid,i,j)) count++;
    return count;
    }
    
    final public boolean paint(final char[][] grid, final int i, final int j){
        if (i<0||i>=grid.length||j<0||j>=grid[0].length||grid[i][j]=='0') {
            return false; 
        }
        
        grid[i][j]='0';
        paint(grid,i,j+1);
        paint(grid,i,j-1);
        paint(grid,i+1,j);
        paint(grid,i-1,j);
        return true;
    }
}
