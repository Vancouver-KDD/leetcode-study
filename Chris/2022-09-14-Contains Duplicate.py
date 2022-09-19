class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Check Rows
        for i in range(9):
            digits = set()
            for j in range(9):
                elem = board[i][j]
                if elem != ".":
                    if elem in digits:
                        return False
                    else:
                        digits.add(elem)
            digits.clear()
                
        # Check Columns
        for i in range(9):
            digits = set()
            for j in range(9):
                elem = board[j][i]
                if elem != ".":
                    if elem in digits:
                        return False
                    else:
                        digits.add(elem)
            digits.clear()
            
            
        # Check Subboxes
        # col : starting column index
        # row : starting row index
        def checkSubbox(row , col):
            subDigits = set()
            for i in range(row, row+3):
                for j in range(col, col+3):
                    elem = board[i][j]
                    if elem != ".":
                        if elem in subDigits:
                            return False
                        else:
                            subDigits.add(elem)
            return True
        
        
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                
                if checkSubbox(i, j) == False:
                    return False
        
        return True