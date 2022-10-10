class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row = [0] * (len(text2)+1)
        matrix = [] 
        for i in range(len(text1)+1):
            matrix.append(row)        
        for col in range(len(text2) -1, -1 ,-1):
            for row in range(len(text1) -1, -1 ,-1):
                if text1[row] == text2[col]:
                    matrix[row][col] = 1 + matrix[row+1][col+1]
                else:
                    matrix[row][col] = max(matrix[row+1][col], matrix[row][col+1])                       
        return matrix[0][0]
