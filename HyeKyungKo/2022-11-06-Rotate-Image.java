//2022.11.06
//Time Complexity: O(NxN)
//Space Complexity: O(1)
class Solution{
    public void rotate(int[][] matrix){
        if(matrix == null || matrix[0].length == 0){
            return;
        }

        int size = matrix.length;

        //Reverse on Diagonal 
        for(int i = 1; i < size; i++ ){
            for(int j = 0; j < i; j++){
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        //and then Reverse Left to Right
        for(int i = 0; i < size ; i++ ){
            for(int j = 0; j < size /2 ; j++){
                int temp = matrix[i][j];
                matrix[i][j] = matrix[i][size - 1 - j];
                matrix[i][size -1 -j] = temp;
            }
        }
    }
}

//Time Complexity: O(NxN)
//Space Complexity: O(1)
//moving 4 points at once (리트코드를 참조해서 수정)
/*
class Solution{
    public void rotate(int[][] matrix){
        if(matrix == null || matrix[0].length == 0){
            return;
        }

        int length = matrix.length;
        for(int i = 0; i < (length +1)/2 ; i++){ // (matrix.length +1) /2 <-- round (half size)
            for(int j = 0; j < length /2 ; j++){ // floor (half size)
                moveCells(matrix, i, j);
            }

        }

    }
    //move 4 cells by 90 degree 
    private void moveCells(int[][] matrix, int row, int col){

        int curr = matrix[row][col];

        for(int i = 0; i < 4; i++){
            int nextRow = col;
            int nextCol = matrix.length -1 - row;
            int next = matrix[nextRow][nextCol];
            matrix[nextRow][nextCol] = curr;
            curr = next;
            row = nextRow;
            col = nextCol;
        }       

    }
}
*/
/*
class Solution {
    public void rotate(int[][] matrix) {
        
        if(matrix == null || matrix[0].length == 0){
            return;
        }

        int rowSize = matrix.length;

        int startRow = rowSize -1;
        int startCol = 0;
        while(startRow >= matrix.length/2){

            if(startRow == startCol){ // center cell in case that 'n' is odd number
                break;
            }
            
            int count = 0;
            while(count < rowSize-1){
                rotate(matrix, startRow - count, startCol);
                count++;
            } 
   
            rowSize -= 2;
            startRow--;   
            startCol++;
        }
    }
    
    //move 4 cells by 90 degree 
    private void moveCells(int[][] matrix, int row, int col){

        int curr = matrix[row][col];

        for(int i = 0; i < 4; i++){
            int nextRow = col;
            int nextCol = matrix.length -1 - row;
            int next = matrix[nextRow][nextCol];
            matrix[nextRow][nextCol] = curr;
            curr = next;
            row = nextRow;
            col = nextCol;
        }       

    }
}
*/