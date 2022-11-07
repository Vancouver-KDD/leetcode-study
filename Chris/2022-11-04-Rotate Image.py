class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        l, r = 0, len(matrix)
        length = len(matrix)
        
        while l < r:
            for i in range(l,r-1):
                tmp = matrix[l][i]
                matrix[l][i] = matrix[length-1-i][l]
                matrix[length-1-i][l] = matrix[r-1][length-1-i]
                matrix[r-1][length-1-i] = matrix[i][r-1]
                matrix[i][r-1] = tmp
            l += 1
            r -= 1
                                                                                                     
            
                
            
        
    