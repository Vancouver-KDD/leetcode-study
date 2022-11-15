class Solution {
    public void rotate(int[][] matrix) {
        int up = 0;
        int down = matrix.length-1;
        while(up < down) {
            for(int j = 0; j < matrix[0].length; j++) {
                int temp = matrix[up][j];
                matrix[up][j] = matrix[down][j];
                matrix[down][j] = temp;
            }
            up++;
            down--;
        }

        for(int i = 0; i < matrix.length; i++) {
            for(int j = 0; j < i; j++) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
    }
}