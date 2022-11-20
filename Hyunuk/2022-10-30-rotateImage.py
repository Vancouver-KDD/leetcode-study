class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        n = len(matrix)
        for r in range(n // 2):
            for i in range(r, n - r - 1):
                matrix[r][i], matrix[i][n - r - 1], matrix[n-r-1][n-i-1], matrix[n-1-i][r] = matrix[n-1-i][r], matrix[r][i], matrix[i][n - r - 1], matrix[n-r-1][n-i-1]
