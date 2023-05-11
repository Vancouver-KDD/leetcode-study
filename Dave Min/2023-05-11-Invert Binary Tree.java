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
    public TreeNode invertTree(TreeNode root) {
        TreeNode node = new TreeNode();
        node = root;
         doInvertTree(node);
         return root;
    }
    public void doInvertTree(TreeNode node) {
        if(node==null) return;

        TreeNode tmpL = node.left;
        TreeNode tmpR = node.right;
        node.left = tmpR;
        node.right = tmpL;
        
        doInvertTree(node.left);
        doInvertTree(node.right);
    }   
}
