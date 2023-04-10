// You are given an n x n 2D matrix representing an image, 
// rotate the image by 90 degrees (clockwise).

// You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
// DO NOT allocate another 2D matrix and do the rotation.

// Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
// Output: [[7,4,1],[8,5,2],[9,6,3]]

// Constraints:

// n == matrix.length == matrix[i].length
// 1 <= n <= 20
// -1000 <= matrix[i][j] <= 1000

//  1. transposing the matrix (rows become columns) and then reverse each row of the matrix
// reverse each row of the matrix by swapping the elements at matrix[i][j] with matrix[i][n-1-j], where n is the length of the row
// time complexity is O(N^2) as we need to traverse the matrix twice 
// space complexity is O(1) since we are rotating the matrix in-place
Return the rotated matrix
public static void rotate(int[][] matrix) {
    int n = matrix.length;
    
    // transpose the matrix
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }
    
    // reverse each row of the matrix
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n/2; j++) {
            int temp = matrix[i][j];
            matrix[i][j] = matrix[i][n-1-j];
            matrix[i][n-1-j] = temp;
        }
    }
}
