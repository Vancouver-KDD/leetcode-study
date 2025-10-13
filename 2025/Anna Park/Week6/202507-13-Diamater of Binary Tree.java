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
class DiameterOfBinaryTree {

    // Variable to store the maximum diameter found so far
    private int maxDiameter = 0;

    // Main function to calculate the diameter of the binary tree
    public int diameterOfBinaryTree(TreeNode root) {
        // Start the depth-first traversal from the root
        depth(root);
        // Return the maximum diameter found
        return maxDiameter;
    }        

    // Helper function to compute the depth of a node
    // and update the max diameter along the way
    public int depth(TreeNode node) {

        // Base case: if the node is null, its depth is 0
        if (node == null) return 0;

        // Recursively get the depth of the left and right subtrees
        int left = depth(node.left);
        int right = depth(node.right);

        // Update the diameter if the path through this node is longer
        maxDiameter = Math.max(maxDiameter, left + right);

        // Return the depth of the current node
        return Math.max(left, right) + 1;
    }
}
