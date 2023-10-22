/*
 * https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
 * 
 * ## Description
 * You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

    struct Node {
    int val;
    Node *left;
    Node *right;
    Node *next;
    }
    Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

    Initially, all next pointers are set to NULL.
 *
 */

 /************************ BFS ************************/

 class Solution {
    public Node connect(Node root) {
        //Set early exit condition 
        if(root == null) return null;

        //q will store the nodes in the same row(level)
        Queue<Node> q = new LinkedList<>();
        
        //store root to start traversing
        q.offer(root);

        //traverse all the nodes with while loop
        while(!q.isEmpty()) {
            //as we are traversing row by row and right to left, set the rightNode as null. 
            Node rightNode = null;
            //iterate x time where x is the number of nodes in a row 
            for(int i = q.size(); i > 0; i--) {
                //store the current node we're pointing to connect
                //use poll() to remove and return the first value from q, so we can calculate the number of nodes in a row again when we move to next row. 
                Node cur = q.poll();
                //connect to rightNode 
                cur.next = rightNode;
                //update the rightNode to current 
                rightNode = cur;

                //if there is children, 
                //note that we are given perfect binary tree, means that if there is right child, there always is left child as well. (vice versa)
                //therefore we don't need to check both condition for left and right
                if(cur.right != null) {
                    //populate q with next level children of current pointer
                    q.offer(cur.right);
                    q.offer(cur.left);
                }
            }
        }
        return root;        
    }
}

//Since we are using Queue to store the nodes, space complexity will be O(n) 
//We can make it O(1) by populating children in advance 

 /************************ Optimized BFS ************************/

 class Solution {
    public Node connect(Node root) {

        //Set early exit condition 
        if(root == null) return null;

        //Store head node to return after traversal 
        Node head = root;

        //traverse all the nodes using while loop 
        //root will be a pointer for a row 
        while(root != null){
            //curr will be point a node in a row 
            for(Node cur = root; cur != null; cur = cur.next) 
                //if there is next row for current pointer, connect the left child to right child. 
                if(cur.left != null) {
                    cur.left.next = cur.right;
                    //if current pointer is not the most right node, we need to connect the right child with the left child of next node.  
                    if(cur.next != null) cur.right.next = cur.next.left;
                } else break; //break if there is no next row. 
            //move to the next row 
            root = root.left;
        }
            
        
        return head;
    }
}