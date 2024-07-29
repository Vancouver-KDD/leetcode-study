/**
 * Leetcode
 * problem: 257
 * link: https://leetcode.com/problems/binary-tree-paths/description/
 * tag: String, Backtracking, Tree, Depth-First Search, Binary Tree
 * ---
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
 * ---
 * 1. dfs algorithm
 * 2. no child, add to result list
 */
class Solution {
    List<String> result;

    public List<String> binaryTreePaths(TreeNode root) {
        result = new ArrayList<String>();
        helper(root, "");
        return result;
    }

    // method for dfs
    private void helper(TreeNode node, String value) {
        if (value.equals("")) {
            value += node.val;
        } else {
            value += "->" + node.val;
        }

        if (node.left == null && node.right == null) {
            result.add(value);
        } else {
            if (node.left != null) {
                dfs(node.left, value);
            }
            if (node.right != null) {
                dfs(node.right, value);
            }
        }
    }
}