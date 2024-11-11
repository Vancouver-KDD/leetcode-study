class TrieNode {
  constructor() {
    this.children = Array(26).fill(null);
    this.endOfword = false;
  }
}

class WordDictionary {
  constructor() {
    this.root = new TrieNode();
  }

  /**
   * @param {string} c
   * @return {number}
   */
  getIndex(c) {
    return c.charCodeAt(0) - "a".charCodeAt(0);
  }

  /**
   * @param {string} word
   * @return {void}
   */
  addWord(word) {
    let cur = this.root;

    for (let c of word) {
      const idx = this.getIndex(c);
      if (cur.children[idx] === null) {
        cur.children[idx] = new TrieNode();
      }
      cur = cur.children[idx];
    }

    cur.endOfword = true;
  }

  /**
   * @param {string} word
   * @return {boolean}
   */
  search(word) {
    return this.dfs(word, 0, this.root);
  }

  dfs(word, j, root) {
    let cur = root;

    for (let i = j; i < word.length; i++) {
      const c = word[i];
      if (c === ".") {
        for (const child of cur.children) {
          if (child !== null && this.dfs(word, i + 1, child)) {
            return true;
          }
        }

        return false;
      } else {
        const idx = this.getIndex(c);
        if (cur.children[idx] === null) {
          return false;
        }
        cur = cur.children[idx];
      }
    }

    return cur.endOfword;
  }
}
