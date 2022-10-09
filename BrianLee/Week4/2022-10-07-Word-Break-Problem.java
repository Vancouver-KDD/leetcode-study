class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Node root = new Node();
        for(String word : wordDict) {
            Node node = root;
            for(char c: word.toCharArray()) {
                if(node.children[c-'a'] == null) {
                    node.children[c-'a'] = new Node();
                }
                node = node.children[c-'a'];
            }
            node.isWord = true;
        }
        return wordFinder(root, root, s, 0, new boolean[s.length()]);
    }

    public boolean wordFinder(Node root, Node node, String s, int cur, boolean[] mem) {
        if(node.isWord == true && cur == s.length()) {
            return true;
        }

        if(cur == s.length()) return false;

        if(node.isWord && !mem[cur]) {
            System.out.println(cur);
            if(wordFinder(root, root, s, cur, mem)) {
                return true;
            } else {
                mem[cur] = true;
            }
        }
        if(node.children[s.charAt(cur)-'a'] != null) {
            if(wordFinder(root, node.children[s.charAt(cur)-'a'], s, cur+1, mem)) {
                return true;
            }
        }
        return false;

    }

    class Node {
        Node[] children;
        boolean isWord;
        public Node() {
            children = new Node[26];
            isWord = false;
        }
    }
}