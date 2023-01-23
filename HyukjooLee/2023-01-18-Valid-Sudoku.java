/**
 * Determine if a 9 x 9 Sudoku board is valid.
 * Only the filled cells need to be validated according to the following rules:
 * Each row must contain the digits 1-9 without repetition.
 * Each column must contain the digits 1-9 without repetition.
 * Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
 */

 class Solution {
    public boolean isValidSudoku(char[][] board) {
    /// check rows
    for (int i = 0; i < 9; i++) {
        boolean[] row = new boolean[9];
        for (int j = 0; j < 9; j++) {
            if (board[i][j] != 0) {
                if (row[board[i][j] - 1]) {
                    return false;
                }
                row[board[i][j] - 1] = true;
            }
        }
    }

    // check columns
    for (int i = 0; i < 9; i++) {
        boolean[] col = new boolean[9];
        for (int j = 0; j < 9; j++) {
            if (board[j][i] != 0) {
                if (col[board[j][i] - 1]) {
                    return false;
                }
                col[board[j][i] - 1] = true;
            }
        }
    }

    // check 3x3 sub-grids
    for (int i = 0; i < 9; i += 3) {
        for (int j = 0; j < 9; j += 3) {
            boolean[] subgrid = new boolean[9];
            for (int x = i; x < i + 3; x++) {
                for (int y = j; y < j + 3; y++) {
                    if (board[x][y] != 0) {
                        if (subgrid[board[x][y] - 1]) {
                            return false;
                        }
                        subgrid[board[x][y] - 1] = true;
                    }
                }
            }
        }
    }

    return true;
}
