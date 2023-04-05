class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroColumnSet = set()
        zeroRowSet = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (matrix[i][j] == 0):
                    zeroColumnSet.add(j)
                    zeroRowSet.add(i)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zeroRowSet:
                    matrix[i][j] = 0
        for j in range(len(matrix[0])):
            for i in range(len(matrix)):
                if j in zeroColumnSet:
                    matrix[i][j] = 0
        