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

import java.util.LinkedList;
import java.util.Queue;

/**
FIRST SOLUTION: using Queue & level order traversal

Time Complexity: O(N) because we iterate trough all nodes in tree
Space Complexity: O(N). Maximum space occupied by the queue is the maximum number of nodes in a level.
In a perfect binary tree, this would be N/2 nodes. Thus O(N/2) = O(N).
 */
class Solution {
    public Node connect(Node root) {
        if(root == null) {
            return root;
        }

        Queue<Node> q = new LinkedList<Node>();
        //start with root
        q.add(root);

        //while each node in tree is visited
        while(q.size() > 0) {
            //size is the number of nodes on the same level
            int size = q.size();
            
            //iterate over the nodes on the same level
            while(size > 0) {
                //get first item from queue
                Node helper = q.remove();

                //this statement is needed because last node's next pointer on a level is null
                //without this statement last node will point to the first node on the next level
                if (size != 1) {
                    helper.next = q.peek();
                }

                //add child nodes (if exist) to q
                if(helper.left != null) {
                    q.add(helper.left);
                }
                if(helper.right != null) {
                    q.add(helper.right);
                }
                size--;
            }

        }


        return root;
    }
}

/**
SECOND SOLUTION: using next pointers
Time Complexity: O(N) because we iterate through all nodes in tree
Space Complexity: O(1) because no extra data structure used
 */
class Solution2 {

    Node prev;
    Node leftmost;

    public Node connect(Node root) {
        if(root == null) {
            return root;
        }

        this.leftmost = root;
        Node curr = leftmost;

        while(this.leftmost != null) {
            this.prev = null;
            curr = this.leftmost;
            //TODO, solution not complete.
        }
        
        return root;
    }
}