"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Input: m = 3, n = 7
Output: 28

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:
1 <= m, n <= 100
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr = [[0]*n]*m

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
        return arr[m - 1][n - 1]

    # O(n * m) O(n)
    def uniquePaths(self, m, n):
        row = [1] * n  # Start from the bottom row where the destination is located

        for i in range(m - 1):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):  # go from right to left
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]

