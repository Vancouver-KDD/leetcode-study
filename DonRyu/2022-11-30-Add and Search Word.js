/**
 * Initialize your data structure here.
 */
var Trie = function() {
    this.root = {};
};

/**
 * Inserts a word into the trie.
 * @param {string} word
 * @return {void}
 */
Trie.prototype.insert = function(word) {
    let node = this.root;
    for(let letter of word) {
        if (node[letter] === undefined) node[letter] = {};
        node = node[letter]
    }
    node.isEnd = true;
};

/**
 * Returns if the word is in the trie.
 * @param {string} word
 * @return {boolean}
 */
Trie.prototype.search = function(word) {
    let node = this.root
    for(let letter of word) {
        // check if current letter is in the node
        if(!node[letter]) {
            return false;
        } else {
            node = node[letter];
        }
    }

    return node && node.isEnd === true;
};

/**
 * Returns if there is any word in the trie that starts with the given prefix.
 * @param {string} prefix
 * @return {boolean}
 */
Trie.prototype.startsWith = function(prefix) {
    let node = this.root;
    for(let letter of prefix) {
        if(!node[letter]) {
            return false;
        } else {
            node = node[letter];
        }
    }
    return true;
};
