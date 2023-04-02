// There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
// The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
// The robot can only move either down or right at any point in time.

// Given the two integers m and n,
// return the number of possible unique paths that the robot can take to reach the bottom-right corner.

// The test cases are generated so that the answer will be less than or equal to 2 * 109.

// Input: m = 3, n = 2
// Output: 3
// Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
// 1. Right -> Down -> Down
// 2. Down -> Down -> Right
// 3. Down -> Right -> Down

// m * n 그리드 보더가 주어지고, 맨 왼쪽 위에서 맨 오른쪽 아래 포인트 까지 이동 할수 있는 paths 의 수를 찾는 문제
// 1. initialize 2D array (size m * n) / from (0, 0) / to (i, j)
// 2. initialize the first row and first column of dp to 1, since there is only one path to reach them
// 3. compute the number of unique paths from above (i-1, j) to left (i, j-1)
// 4. return the number of unique paths

// time complexity is O(MN): the number of unique paths for each cell
// space complexity is O(MN): 2D array M * N to store the dp vals
public static int uniquePaths(int rows, int cols) {
    // 1.
    int[][] numPaths = new int[rows][cols];
    
    // 2.
    for (int i = 0; i < rows; i++) {
        numPaths[i][0] = 1;
    }
    for (int j = 0; j < cols; j++) {
        numPaths[0][j] = 1;
    }
    
    // 3. 
    for (int row = 1; row < rows; row++) {
        for (int col = 1; col < cols; col++) {
            numPaths[row][col] = numPaths[row-1][col] + numPaths[row][col-1];
        }
    }
    
    // 4.
    return numPaths[rows-1][cols-1];
}
