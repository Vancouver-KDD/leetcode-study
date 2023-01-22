class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_size = 9
        rows_digits = [set() for _ in range(board_size)]
        cols_digits = [set() for _ in range(board_size)]
        box_digits = [[set() for _ in range(board_size//3)] for _ in range(board_size//3)]

        for i in range(board_size):
            for j in range(board_size):
                digit = board[i][j]
                if digit != ".":
                    if digit in rows_digits[i]:
                        return False
                    if digit in cols_digits[j]:
                        return False
                    if digit in box_digits[i//3][j//3]:
                        return False
                    rows_digits[i].add(digit)
                    cols_digits[j].add(digit)
                    box_digits[i//3][j//3].add(digit)
        return True
