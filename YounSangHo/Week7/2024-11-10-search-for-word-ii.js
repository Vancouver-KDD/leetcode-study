class TrieNode {
  constructor() {
    this.children = {};
    this.isWord = false;
  }

  /**
   * @param {string} word
   * @return {void}
   */
  addWord(word) {
    let cur = this;
    for (const c of word) {
      if (!(c in cur.children)) {
        cur.children[c] = new TrieNode();
      }
      cur = cur.children[c];
    }
    cur.isWord = true;
  }
}

class Solution {
  /**
   * @param {character[][]} board
   * @param {string[]} words
   * @return {string[]}
   */
  findWords(board, words) {
    const root = new TrieNode();
    for (const word of words) {
      root.addWord(word);
    }

    const ROWS = board.length,
      COLS = board[0].length;
    const res = new Set(),
      visit = new Set();

    const dfs = (r, c, node, word) => {
      if (
        r < 0 ||
        c < 0 ||
        r >= ROWS ||
        c >= COLS ||
        visit.has(`${r},${c}`) ||
        !(board[r][c] in node.children)
      ) {
        return;
      }

      visit.add(`${r},${c}`);
      node = node.children[board[r][c]];
      word += board[r][c];
      if (node.isWord) {
        res.add(word);
      }

      dfs(r + 1, c, node, word);
      dfs(r - 1, c, node, word);
      dfs(r, c + 1, node, word);
      dfs(r, c - 1, node, word);

      visit.delete(`${r},${c}`);
    };

    for (let r = 0; r < ROWS; r++) {
      for (let c = 0; c < COLS; c++) {
        dfs(r, c, root, "");
      }
    }

    return Array.from(res);
  }
}
