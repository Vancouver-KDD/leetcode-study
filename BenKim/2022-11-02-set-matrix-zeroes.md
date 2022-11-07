# 73. Set Matrix Zeroes

> Problem link: https: https://leetcode.com/problems/set-matrix-zeroes/  
> submission detail: https://leetcode.com/submissions/detail/835258102/  

```py
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = 1

        # use first row, colum to mark zero line
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    # set 0 at top row
                    matrix[0][c] = 0

                    # set 0 to left col
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero = 0

        # set 0 to inside matrix
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # set 0 to all left col
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0

        # set 0 to all top col
        if rowZero == 0:
            for c in range(COLS):
                matrix[0][c] = 0
        
        
```