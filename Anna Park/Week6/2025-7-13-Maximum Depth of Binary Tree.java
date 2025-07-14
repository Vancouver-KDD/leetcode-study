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
class MaximumDepthofbinaryTree {

    int maxDepth = 0;

    public int maxDepth(TreeNode root) {
        
        if (root == null) return 0;
        maxDepth++; 
        depth(root);
        return maxDepth;
    }

    public int depth(TreeNode node){
        
        if (node == null) return 0;
        else maxDepth++;

        int left = depth(node.left);
        int right = depth(node.right);

        maxDepth = Math.max(left, right);
        return Math.max(left, right) + 1;
    }
}
