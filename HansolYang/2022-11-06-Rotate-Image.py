class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        for r in range(n//2):
            for c in range(r, n-r-1):
                matrix[r][c], matrix[c][n-r-1], matrix[n-r-1][n-c-1], matrix[n-c-1][r] = matrix[n-c-1][r], matrix[r][c], matrix[c][n-r-1], matrix[n-r-1][n-c-1]