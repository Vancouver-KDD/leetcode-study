// Design a data structure that supports adding new words and finding if a string matches any previously added string.

// Implement the WordDictionary class:

// WordDictionary() Initializes the object.
// void addWord(word) Adds word to the data structure, it can be matched later.
// bool search(word) Returns true if there is any string in the data structure
// that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

class TrieNode {
    private TrieNode[] children;
    private boolean isEnd;

    public TrieNode() {
        children = new TrieNode[26];
        isEnd = false;
    }

    public boolean containsKey(char c) {
        return children[c - 'a'] != null;
    }

    public TrieNode get(char c) {
        return children[c - 'a'];
    }

    public void put(char c, TrieNode node) {
        children[c - 'a'] = node;
    }

    public boolean isEnd() {
        return isEnd;
    }

    public void setEnd() {
        isEnd = true;
    }
}

class WordDictionary {
    private TrieNode root;

    public WordDictionary() {
        root = new TrieNode();
    }

    public void addWord(String word) {
        TrieNode node = root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (!node.containsKey(c)) {
                node.put(c, new TrieNode());
            }
            node = node.get(c);
        }
        node.setEnd();
    }

    public boolean search(String word) {
        return searchHelper(word, 0, root);
    }

    private boolean searchHelper(String word, int index, TrieNode node) {
        if (index == word.length()) {
            return node.isEnd();
        }
        char c = word.charAt(index);
        if (c == '.') {
            for (int i = 0; i < 26; i++) {
                if (node.containsKey((char) ('a' + i))) {
                    if (searchHelper(word, index + 1, node.get((char) ('a' + i)))) {
                        return true;
                    }
                }
            }
        } else {
            if (node.containsKey(c)) {
                return searchHelper(word, index + 1, node.get(c));
            }
        }
        return false;
    }
}
