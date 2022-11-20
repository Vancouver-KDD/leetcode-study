//2022.10.23

//limitation : if heights is null or size is zero, return empty list 
//Time Complexity: O(MxN)
//Space Complexity: O(MxN)

class Solution {
    
    private final int[][] DIRECTIONS = new int[][]{{-1, 0}, {0, -1}, {0, 1}, {1, 0}}; //left, up, right, down
    
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        
        List<List<Integer>> bothOceansFlow = new ArrayList<List<Integer>>();
        
        if(heights == null || heights.length == 0 || heights[0].length == 0){
            return bothOceansFlow;
        }
        
        int rowSize = heights.length;
        int colSize = heights[0].length;
        
        boolean[][] pacificFlow = new boolean[rowSize][colSize];
        boolean[][] atlanticFlow = new boolean[rowSize][colSize];
        
        //find the cell that flow toward pacific or altantic 
        for(int i = 0; i < rowSize; i++){
            visitIsland(heights, i, 0, pacificFlow); // start from upper boundary - pacific
            visitIsland(heights, i, colSize-1, atlanticFlow); //start from lower boundary - atlanticflow
        }
        for(int i = 0; i < colSize; i++){
            visitIsland(heights, 0, i, pacificFlow); //start from left boundary - pacific
            visitIsland(heights, rowSize-1, i, atlanticFlow); // start from right boundary - atlanticflow
        }
        
        for(int i = 0; i < rowSize; i++){
            for(int j = 0; j < colSize; j++){
                if(pacificFlow[i][j] && atlanticFlow[i][j]){
                    bothOceansFlow.add(Arrays.asList(i, j));
                }
            }
        }
        
        return bothOceansFlow;
    }
    
    private void visitIsland(int[][] heights, int row, int col, boolean[][] oceanFlow){
        
        int rowSize = heights.length;
        int colSize = heights[0].length;
        
        if(row < 0 || row >= rowSize || col < 0 || col >= colSize){
            return;
        }
        
        oceanFlow[row][col] = true; // mark visited
        
        for(int[] direc : DIRECTIONS){
            int newRow = row + direc[0];
            int newCol = col + direc[1];
            
            //check if it is out of boundary
            if(newRow < 0 || newRow >= rowSize || newCol < 0 || newCol >= colSize){
                continue;
            }
                        
            //if it is already visited, skip 
            if(oceanFlow[newRow][newCol]){
                continue;
            }
            
            if(heights[newRow][newCol] < heights[row][col]){
                continue;
            }

            //visit the new cell
            visitIsland(heights, newRow, newCol, oceanFlow);
            
        }
        
    }
}
