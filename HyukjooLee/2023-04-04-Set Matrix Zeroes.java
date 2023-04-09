// Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
// You must do it in place.

// Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
// Output: [[1,0,1],[0,0,0],[1,0,1]]

// Constraints:

// m == matrix.length
// n == matrix[0].length
// 1 <= m, n <= 200
// -231 <= matrix[i][j] <= 231 - 1

// A straightforward solution using O(mn) space is probably a bad idea.
// A simple improvement uses O(m + n) space, but still not the best solution.
// Could you devise a constant space solution?

// In-place algorithm 이란,
// 추가적인 메모리 공간을 사용하지 않고, 주어진 입력 값들을 직접적으로 변경하면서 알고리즘을 수행하는 것
// 입력값의 크기가 매우 크거나, 메모리 공간이 제한된 환경에서 유용

// 장점: 추가적인 배열을 사용하지 않고도 주어진 배열의 요소들을 직접적으로 교환하여 정렬
// 단점: 입력값을 직접적으로 변경하기 때문에 입력값이 다른 부분에서 사용될 수 있는 경우, 예기치 않은 결과 도출 가능
// In-place algorithm 을 사용할 때는 주어진 입력값을 미리 백업해 두는 등의 방법을 사용하여 예기치 않은 결과를 방지해야 함


// 1. using two sets to keep track of the rows and columns that need to be zero
// first traverse the matrix once to identify the rows and columns that contain a zero
// then we traverse the matrix again to zero out the identified rows and columns
class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        Set<Integer> rows = new HashSet<>();
        Set<Integer> cols = new HashSet<>();
        
        // identify rows and columns that need to be zeroed
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == 0) {
                    rows.add(i);
                    cols.add(j);
                }
            }
        }
        
        // zero out rows and columns
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (rows.contains(i) || cols.contains(j)) {
                    matrix[i][j] = 0;
                }
            }
        }
    }
}


// 2. using constant space by using the first row and first column of the matrix
// in order to keep track of the rows and columns that need to be zero
// first check if the first row and first column need to be zero
// two boolean variables to indicate whether the first row and first column need to be zero
// then...
class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        boolean firstRowZero = false, firstColZero = false;
        
        // check if first row and first column need to be zeroed out
        for (int i = 0; i < m; i++) {
            if (matrix[i][0] == 0) {
                firstColZero = true;
                break;
            }
        }
        for (int j = 0; j < n; j++) {
            if (matrix[0][j] == 0) {
                firstRowZero = true;
                break;
            }
        }
        
        // mark corresponding element in first row and first column to zero if current element is zero
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][j] == 0) {
                    matrix[i][0] = 0;
                    matrix[0][j] = 0;
                }
            }
        }
        
        // zero out rows and columns based on values in first row and first column
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (matrix[i][0] == 0 || matrix[0][j] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }
        
        // zero out first row and first column if necessary
        if (firstRowZero) {
            for (int j = 0; j < n; j++) {
                matrix[0][j] = 0;
            }
        }
        if (firstColZero) {
            for (int i = 0; i < m; i++) {
                matrix[i][0] = 0;
            }
        }
    }
}
