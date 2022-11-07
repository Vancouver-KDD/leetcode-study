class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        for c in range(len(matrix[0])): #iterate 2-D in order of r->c
            for r in range(len(matrix)):
                
                if matrix[r][c] == 0:
                    for i in range(len(matrix)):
                        matrix[i][c] = 'c' if matrix[i][c] != 0 else 0
                    for j in range(len(matrix[0])):
                        matrix[r][j] = 'c' if matrix[r][j] != 0 else 0
        
        for c in range(len(matrix[0])):
            for r in range(len(matrix)):
                if matrix[r][c] == 'c':
                    matrix[r][c] = 0
        
        return matrix