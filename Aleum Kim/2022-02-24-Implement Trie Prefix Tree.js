class TrieNode {
    constructor() {
        this.children = {};
        this.isWord = false;
    }
}

class Trie {
    constructor() {
        this.root = new TrieNode();
    }

    /* Time O(N) | Space O(N) */
    insert(word, node = this.root) {
        for (const char of word) {
            const child = node.children[char] || new TrieNode();

            node.children[char] = child;

            node = child;
        }

        node.isWord = true;
    }

    /* Time O(N) | Space O(1) */
    search(word, node = this.root) {
        for (const char of word) {
            const child = node.children[char] || null;

            if (!child) return false;

            node = child;
        }

        return node.isWord;
    }

    /* Time O(N) | Space O(1) */
    startsWith(prefix, node = this.root) {
        for (const char of prefix) {
            const child = node.children[char] || null;

            if (!child) return false;

            node = child;
        }

        return true;
    }
}