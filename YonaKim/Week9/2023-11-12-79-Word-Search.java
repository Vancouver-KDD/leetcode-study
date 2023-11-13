class Solution {
  private char[][] board;
  private int numRows;
  private int numCols;

  public boolean searchWord(char[][] gameBoard, String targetWord) {
    this.board = gameBoard;
    this.numRows = gameBoard.length;
    this.numCols = gameBoard[0].length;

    for (int row = 0; row < numRows; ++row)
      for (int col = 0; col < numCols; ++col)
        if (backtrackSearch(row, col, targetWord, 0))
          return true;
    return false;
  }
  
  protected boolean backtrackSearch(int row, int col, String word, int index) {
    // Base case of recursion. If the word to be matched is empty, return true.
    if (index >= word.length())
      return true;

    // Check if the current state is invalid:
    // If the letter in the current cell does not match the first letter of the word,
    // or if the position of the cell is out of the boundary of the board.
    if (row < 0 || row == numRows || col < 0 || col == numCols
        || board[row][col] != word.charAt(index))
      return false;

    /* Step 3). Explore the neighbors in DFS */
    // Explore neighbors in DFS (backtracking)
    // Mark the current cell as visited (using any non-alphabetic letter)
    // Then iterate through the up, down, right, left directions (order of direction does not matter)
    boolean result = false;
    // Mark the path before the next exploration
    board[row][col] = '#';

    int[] rowOffsets = {0, 1, 0, -1};
    int[] colOffsets = {1, 0, -1, 0};
    for (int direction = 0; direction < 4; ++direction) {
      result = backtrackSearch(row + rowOffsets[direction], col + colOffsets[direction], word, index + 1);
      if (result)
        break;
    }

    // Revert the cell back to its original state
    // Return the result of recursion
    board[row][col] = word.charAt(index);
    return result;
  }
}
