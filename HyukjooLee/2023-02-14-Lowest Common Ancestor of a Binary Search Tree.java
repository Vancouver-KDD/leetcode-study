// Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

// According to the definition of LCA on Wikipedia: 
// “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as 
// descendants (where we allow a node to be a descendant of itself).”

// Note a BST's property 
// for the given node N
// all the nodes in its left subtree have values less than N, 
// and all the nodes in its right subtree have values greater than N.

// 1. using recursive approach
// if the current node is greater than two given nodes (p , q), p and q must be in the left subtree
// if the current node is smaller than two given nodes (p , q), p and q must be in the right subtree
// if the current node is between p and q, the node is the lowest common ancestor
// because it is the node that is able to have p and q as children in BST
// time complexity is O(H) - Height if the binary search tree
// space complexity is O(H) -  the maximum number of function calls 
// that can be stored on the call stack at any given time is equal to the height of the tree.

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // if the current node is greater than two given nodes (p , q), p and q must be in the left subtree
        if(root.val > p.val && root.val > q.val) return lowestCommonAncestor(root.left, p, q);
        // if the current node is smaller than two given nodes (p , q), p and q must be in the right subtree
        if(root.val < p.val && root.val < q.val) return lowestCommonAncestor(root.right, p, q);
        // if the current node is between p and q, the node is the lowest common ancestor       
        return root;      
    }
}

// 2. using iterative 
// Time - O(H) in worst case(not balanced), the height of the BST ; if balanced, O(logN)
// Space - O(H)
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        int pVal = p.val;
        int qVal = q.val;

        TreeNode node = root;

        while(node != null) {
            int rootVal = node.val;

            if(rootVal > pVal && rootVal > qVal) {
                node = node.left;
            } else if (rootVal < pVal && rootVal < qVal) {
                node = node.right;
            } else {
                return node;
            }
        } 

        return node;  
    }
}