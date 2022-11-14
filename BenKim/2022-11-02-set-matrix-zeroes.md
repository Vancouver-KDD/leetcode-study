# 73. Set Matrix Zeroes

> Problem link: https: https://leetcode.com/problems/set-matrix-zeroes/  
> submission detail:   
> - https://leetcode.com/submissions/detail/835258102/  
> - https://leetcode.com/problems/set-matrix-zeroes/submissions/839261844/

## 1. using extra array
```py
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # TC: O(m * n)
        # SC: O(m + n)
        ROWS = len(matrix) #m
        COLS = len(matrix[0]) #n

        # 1. make a extra array to mark zero line
        zeroMarkRow = [1] * ROWS
        zeroMarkCol = [1] * COLS
        
        # 2. loop the every cell of matrix 
        for r in range(ROWS):
            for c in range(COLS):
                # 3. mark to extra row, column when I meet 0
                if(matrix[r][c] == 0):
                    zeroMarkRow[r] = 0
                    zeroMarkCol[c] = 0
            
        # 4. set 0 to zero line
        for r in range(ROWS):
            for c in range(COLS):
                if(zeroMarkRow[r] == 0 or zeroMarkCol[c] == 0):
                    matrix[r][c] = 0
            
        # 5. finish
```

## 2. with hashmap(or set)
```py
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroRows = set()
        zeroCols = set()
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zeroRows.add(r)
                    zeroCols.add(c)
    
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in zeroRows or c in zeroCols:
                    matrix[r][c] = 0
        
```

## 3. without extra array
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