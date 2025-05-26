var TrieNode = function () {
  this.children = {};
  this.endOfWord = false;
};

var Trie = function () {
  this.root = new TrieNode();
};

/**
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function (word) {
  let current = this.root;
  for (let i = 0; i < word.length; i++) {
    let character = word[i];
    if (!(character in current.children)) {
      current.children[character] = new TrieNode();
    }
    current = current.children[character];
  }
  current.endOfWord = true;
};

/**
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function (word) {
  let current = this.root;
  for (let i = 0; i < word.length; i++) {
    let character = word[i];
    if (!(character in current.children)) {
      return false;
    }
    current = current.children[character];
  }
  return current.endOfWord;
};

/**
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function (prefix) {
  let current = this.root;
  for (let i = 0; i < prefix.length; i++) {
    let character = prefix[i];
    if (!(character in current.children)) {
      return false;
    }
    current = current.children[character];
  }
  return true;
};

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
