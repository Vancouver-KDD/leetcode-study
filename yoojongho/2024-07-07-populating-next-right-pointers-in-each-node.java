/**
 * Leetcode
 * problem: 116
 * link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
 * tag: Linked List, Tree, Depth-First Search, Breadth-First Search, Binary Tree
 */

/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/
class Solution {
    private Map<Integer, Node> cache;

    public Node connect(Node root) {
        cache = new HashMap();
        helper(root, 0);
        return root;
    }

    private void helper(Node node, int idx){
        if(node == null) return;
        Node prev = cache.get(idx);
        if(prev == null) {
            cache.put(idx, node);
        }else{
            node.next = prev;
            cache.put(idx, node);
        }
        helper(node.left, idx++);
        helper(node.right, idx++);
    }
}