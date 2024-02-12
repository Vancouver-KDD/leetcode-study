https://leetcode.com/problems/delete-node-in-a-bst/description/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode deleteNode(TreeNode root, int key) {
        if(root == null) return root;
        if(root.val == key && root.left == null && root.right == null) return null;

        TreeNode parent = findParentNodeOfDeleteNode(root, key);
        if(parent == null) return root;
        TreeNode newRoot = deleteOper(parent,key);
        return newRoot == null?root:newRoot;
    }

    private TreeNode findParentNodeOfDeleteNode(TreeNode node, int key) {
        if(node.val == key) return node;
        if(node.val < key) {
            if(node.right != null) {
                if(node.right.val == key) return node;
                else return findParentNodeOfDeleteNode(node.right, key);
            }
        } else {
            if(node.left != null) {
                if(node.left.val == key) return node;
                else return findParentNodeOfDeleteNode(node.left, key);
            }
        }
        return null;
    }

    private TreeNode deleteOper(TreeNode parent, int key) {
        if(parent.val == key) {
            return getExchangedNode(parent);
        } else if(parent.left != null && parent.left.val == key){
            parent.left = getExchangedNode(parent.left);
            return null;
        } else if(parent.right != null && parent.right.val == key){
            parent.right = getExchangedNode(parent.right);
            return null;
        }
        return null;
    }

    private TreeNode getExchangedNode(TreeNode node) {
        if(node == null) return null;
        if(node.right == null) {
            return node.left;
        } else if(node.left == null) {
            return node.right;
        } else {
            TreeNode left = node.left;
            TreeNode right = node.right;
            node = node.right;
            while(node.left != null) {
                node = node.left;
            }
            node.left = left;
            return right;
        }
    }
}