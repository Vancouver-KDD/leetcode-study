class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row = 1
        row, col = len(matrix), len(matrix[0])
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i != 0:
                        matrix[i][0] = 0
                    else:
                        first_row = 0
        
        for i in range(1,row):
            for j in range(1, col):
                if matrix[0][j] == 0 or (i != 0 and matrix[i][0] == 0):
                    matrix[i][j] = 0
                if i == 0 and first_row == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i, row in enumerate(matrix):
                row[0] = 0
        if first_row == 0:
            for j, elem in enumerate(matrix[0]):
                matrix[0][j] = 0