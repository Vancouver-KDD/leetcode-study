//2022.11.05
//Time Complexity: O(MxN)
//Space Complexity: O(M+N)
class Solution {
    public void setZeroes(int[][] matrix) {
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0){
            return;
        }

        HashSet<Integer> rowSet = new HashSet<>();
        HashSet<Integer> colSet = new HashSet<>();

        int rowSize = matrix.length;
        int colSize = matrix[0].length;
        
        for(int i = 0; i < rowSize; i++){
            for(int j = 0; j < colSize; j++){
                if(matrix[i][j] == 0){
                    rowSet.add(i);
                    colSet.add(j);
                }
            }
        }

        for(int i = 0; i < rowSize; i++){
            if(rowSet.contains(i)){
                for(int j = 0; j < colSize; j++){
                    matrix[i][j] = 0;
                }
            }
        }

        for(int j = 0; j < colSize; j++){
            if(colSet.contains(j)){
                for(int i = 0; i < rowSize; i++){
                    matrix[i][j] = 0; 
                }
            }
        }

    }
}