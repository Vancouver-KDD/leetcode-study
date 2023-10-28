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
/**
Time Complexity: O(N). Go through each node once.
Space Complexity: O(N) or O(logN). Depends on the size of the implicit call stack during DFS (height of tree). O(N) = worst case, skewed tree. O(logN) = balanced tree.
 */
class Solution {
    int diameter;
    public int diameterOfBinaryTree(TreeNode root) {
        longestPath(root);
        return diameter;
    }

    public int longestPath(TreeNode node) {
        if(node == null) {
            return 0;
        }

        int leftPath = longestPath(node.left);
        int rightPath = longestPath(node.right);

        diameter = Math.max(diameter, (leftPath + rightPath));

        return Math.max(leftPath, rightPath) + 1;
    }
}