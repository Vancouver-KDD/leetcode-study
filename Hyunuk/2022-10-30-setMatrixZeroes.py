class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        def set_zero(y, x):
            for i in range(r):
                matrix[i][x] = 0
            for j in range(c):
                matrix[y][j] = 0
                
                
        if not matrix or not matrix[0]:
            return
        r, c = len(matrix), len(matrix[0])
        stk = []
        
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    stk.append((i, j))
        while stk:
            (i, j) = stk.pop()
            set_zero(i, j)
        return
