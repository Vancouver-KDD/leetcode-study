// Given an m x n matrix, return all elements of the matrix in spiral order.

// Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
// Output: [1,2,3,6,9,8,7,4,5]

// Constraints:

// m == matrix.length
// n == matrix[i].length
// 1 <= m, n <= 10
// -100 <= matrix[i][j] <= 100

// 2D matrix 을 왼쪽 위 모서리에서 시작하여 시계 방향으로 이동, 나선형 순서로

// 1. traversing a 2D matrix in spiral order, 
// starting from the top left corner and moving clockwise until all elements have been visited
// time complexity is O(NM) since we visit every element in the matrix once
// space complexity is also O(NM) as we store all the elements in the list
class Solution {
    public static List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        int numRows = matrix.length; 
        int numCols = matrix[0].length; 
        int topRow = 0;
        int bottomRow = numRows - 1;
        int leftCol = 0; 
        int rightCol = numCols - 1; 

        // traverse matrix until all elements have been visited
        while (result.size() < numRows * numCols) { 
            // traverse top row from left to right
            for (int col = leftCol; col <= rightCol && result.size() < numRows * numCols; col++) {
                result.add(matrix[topRow][col]);
            }
            topRow++;
            
            // traverse right column from top to bottom
            for (int row = topRow; row <= bottomRow && result.size() < numRows * numCols; row++) {
                result.add(matrix[row][rightCol]);
            }
            rightCol--;
            
            // traverse bottom row from right to left
            for (int col = rightCol; col >= leftCol && result.size() < numRows * numCols; col--) {
                result.add(matrix[bottomRow][col]);
            }
            bottomRow--; 
            
            // traverse left column from bottom to top
            for (int row = bottomRow; row >= topRow && result.size() < numRows * numCols; row--) {
                result.add(matrix[row][leftCol]);
            }
            leftCol++;
        }
        
        return result;
    }

}