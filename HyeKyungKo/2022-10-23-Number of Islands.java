//2022.10.23
//Time Complexity: O(MxN)
//Space Complexity: O(MxN)
class Solution{    
    
    public int numIslands(char[][] grid){
        
        if(grid == null || grid.length == 0 || grid[0].length == 0){
            return 0;
        }
        
        int rowSize = grid.length;
        int colSize = grid[0].length;
        
        int totalNumber = 0;
        
        for(int i = 0; i < rowSize; i++){
            for(int j = 0; j < colSize; j++){
                if(grid[i][j] == '1'){
                    visitIslands(grid, i, j);                                 
                    totalNumber++;
                }

            }
        }
        
        return totalNumber;
    }
    
    private void visitIslands(char[][] grid, int row, int col){
        
        int rowSize = grid.length;
        int colSize = grid[0].length;
        
        if(row < 0 || row >= rowSize || col < 0 || col >= colSize){
            return;
        }
        
        if(grid[row][col] == '0'){ // ocean
            return;
        }
        
        grid[row][col] = '0'; //check as visited
        
        visitIslands(grid, row-1, col); //left
        visitIslands(grid, row, col-1); // up
        visitIslands(grid, row+1, col); //right
        visitIslands(grid, row, col+1); //down        
        
    }
}