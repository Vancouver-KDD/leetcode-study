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

/**
Time Complexity: O(N) because we iterate the nodes in the tree once.
Space Complexity: O(1) because we don't use additional data structures.
 */
class Solution {
    public Node connect(Node root) {
        if(root == null) {
            return root;
        }

        Node leftmost = root;

        //until we reach the second to last level. (we operate one level down.)
        while(leftmost.left != null) {
            Node helper = leftmost;

            //startomg from the leftmost node, we iterate over the nodes on the same level.
            while(helper != null) {
                //connection between two children of a node
                helper.left.next = helper.right;
                //connection between children of the two adjacent nodes.
                if(helper.next != null) {
                    helper.right.next = helper.next.left;
                }
                helper = helper.next;
            }
            //go one level down
            leftmost = leftmost.left;
        }

        return root;
    }
}