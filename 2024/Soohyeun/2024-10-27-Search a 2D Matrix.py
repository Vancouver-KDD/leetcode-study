class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_min = 0
        row_max = len(matrix) - 1
        col_min = 0
        col_max = len(matrix[0]) - 1
        row = 0

        while row_min <= row_max:
            row = (row_min + row_max) // 2

            if matrix[row][col_min] > target:
                # target must be in previous rows or not exist
                row_max = row - 1
                continue
            elif matrix[row][col_max] < target:
                # target must be in later rows or not exist
                row_min = row + 1
            else:
                # target must be in current row
                break
        if row_min > row_max:
            return False
        curr_row = matrix[row]
        while col_min <= col_max:
            col = (col_min + col_max) // 2
            if curr_row[col] < target:
                col_min = col + 1
            elif curr_row[col] > target:
                col_max = col - 1
            else:
                return True
        return False
