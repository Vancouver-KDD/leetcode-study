// Given an m x n grid of characters board and a string word, return true if word exists in the grid.

// The word can be constructed from letters of sequentially adjacent cells,
// where adjacent cells are horizontally or vertically neighboring.
// The same letter cell may not be used more than once.

class Solution {
    public boolean exist(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;
        
        // iterate through each cell on the board
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == word.charAt(0)) {
                    // start the backtracking algorithm
                    if (backtrack(board, word, i, j, 0)) {
                        return true;
                    }
                }
            }
        }
        
        // word not found on the board
        return false;
    }
    
    private boolean backtrack(char[][] board, String word, int i, int j, int index) {
        // all characters found
        if (index == word.length()) {
            return true;
        }
        
        // out of bounds or character doesn't match
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || board[i][j] != word.charAt(index)) {
            return false;
        }
        
        // mark cell as visited
        board[i][j] = '#';
        
        // check adjacent cells
        boolean result = backtrack(board, word, i+1, j, index+1) ||
                         backtrack(board, word, i-1, j, index+1) ||
                         backtrack(board, word, i, j+1, index+1) ||
                         backtrack(board, word, i, j-1, index+1);
        
        // mark cell as unvisited
        board[i][j] = word.charAt(index);
        
        return result;
    }
}
