/*
// Definition for a Node.
public class Node {
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
}
*/

public class Solution {
    List<List<Node>> list = new();
    public Node Connect(Node root) {
        DoTraversal(root,0);
        return root;
    }
    public void DoTraversal(Node node, int lev){
        if(node == null) return;
        if(list.Count < lev+1){
            list.Add(new List<Node>());
        }
        node.next = null;
        
        //if the current level is more than 0, 
        //then there is the left node at the same level which should point to the current node.
        if(list[lev].Count > 0){
            //Console.WriteLine(list[lev][list[lev].Count-1].val);
            (list[lev][list[lev].Count-1]).next = node;
        }
        //Add the node at the current level.
        list[lev].Add(node);

        lev++;
        
        //Since the preorder traversal visits at the particular level in order, 
        //by having the current level, we can keep track of the node at the same level in order
        DoTraversal(node.left,lev);
        DoTraversal(node.right,lev);
        return;
    }
}
