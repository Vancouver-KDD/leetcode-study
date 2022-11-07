//2022.11.05
//Time Complexity : O(mXn)
//Space Complexity: O(1)
class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {

        List<Integer> spiralList = new ArrayList<>();

        if(matrix == null || matrix.length == 0 || matrix[0].length == 0){
            return spiralList;
        }
        
        //RIGHT, DOWN, LEFT, UP
        int[][] move = {{0,1},{1,0},{0,-1},{-1, 0}};
        
        int rowSize = matrix.length -1; //initial moving length for row
        int colSize = matrix[0].length; //initial moviing length for col

        int direction = 0; // 0:RIGHT, 1:DOWN, 2:LEFT, 3:UP
        int row = 0; //initial value
        int col = -1;    //initial value
        int totalCell = matrix.length * matrix[0].length;
        while(spiralList.size() < totalCell){
            int size = 0;
            if(direction % 2 == 0){ //RIGHT or LEFT
                size = colSize;
            }else{  // DOWN or UP
                size = rowSize;
            }

            for(int i = 0; i < size; i++){
                row += move[direction][0];
                col += move[direction][1];
                int value = matrix[row][col];
                spiralList.add(value);
            }

            if(direction % 2 == 0){ //RIGHT or LEFT
                colSize--;
            }else{  // DOWN or UP
                rowSize--;
            }
            //direction change
            direction = (direction+1) % 4;
        }

        return spiralList;
    }
}