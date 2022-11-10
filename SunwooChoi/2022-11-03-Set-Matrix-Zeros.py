class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 0,0 point duplicate to mark col and row is zero
        # additional variable to mark first col should be zero or not
        fir_col = False
        
        # mark row and col if the current value is zero
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                fir_col = True
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # set matrix to zero except first col and row
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        # set first row to zero
        if matrix[0][0] == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
                
        # set first col to zero
        if fir_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0

