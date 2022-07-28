class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowDict = {}
        colDict = {}
        
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):    
                if matrix[i][j] == 0:
                    rowDict[i] = True
                    colDict[j] = True
            
            
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rowDict or j in colDict:
                    matrix[i][j] = 0
        
        # TC : O(mn) 
        # SC : O(m+n)