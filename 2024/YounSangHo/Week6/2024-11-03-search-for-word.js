class Solution {
  /**
   * @param {character[][]} board
   * @param {string} word
   * @return {boolean}
   */
  exist(board, word) {
    const ROWS = board.length;
    const COLS = board[0].length;
    const path = new Set();

    const dfs = (r, c, i) => {
      if (i === word.length) return true;
      if (
        r < 0 ||
        c < 0 ||
        r >= ROWS ||
        c >= COLS ||
        board[r][c] !== word[i] ||
        path.has(`${r},${c}`)
      ) {
        return false;
      }

      path.add(`${r},${c}`);
      const res =
        dfs(r + 1, c, i + 1) ||
        dfs(r - 1, c, i + 1) ||
        dfs(r, c + 1, i + 1) ||
        dfs(r, c - 1, i + 1);
      path.delete(`${r},${c}`);
      return res;
    };

    for (let r = 0; r < ROWS; r++) {
      for (let c = 0; c < COLS; c++) {
        if (dfs(r, c, 0)) return true;
      }
    }
    return false;
  }
}
