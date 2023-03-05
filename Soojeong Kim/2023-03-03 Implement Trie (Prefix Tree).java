class Trie {

    class Node {
        Node [] childs;
        boolean isEnd;
        
        Node(){
            //character
            childs = new Node[26];
            isEnd = false;
        }
    }
    
    final private Node root;

    public Trie() {
        root = new Node();
    }
    
    public void insert(String word) {
        Node curr = root;

        for(int i = 0; i<word.length();i++) {
            //apple
            char ch = word.charAt(i);

            if(curr.childs[ch-'a'] == null ) {
                //if null, make a new node;
                curr.childs[ch-'a'] = new Node(); //a로 시작하는 node
            }
            curr = curr.childs[ch-'a'];
        }
        //insert 했기 때문에, true
        curr.isEnd = true;
        
    }
    
    public boolean search(String word) {
        Node curr = root;

        for(int i = 0; i<word.length();i++) {
            char ch = word.charAt(i);

            if(curr.childs[ch-'a'] == null) {
                return false;
            }
            curr = curr.childs[ch-'a'];
        }
        return curr.isEnd;
    }
    
    public boolean startsWith(String prefix) {
        Node curr = root;

        for(int i = 0; i<prefix.length();i++) {
            char ch = prefix.charAt(i);

            if(curr.childs[ch-'a']==null){
                return false;
            }
            curr = curr.childs[ch-'a'];
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */

 //https://leetcode.com/problems/implement-trie-prefix-tree/editorial/