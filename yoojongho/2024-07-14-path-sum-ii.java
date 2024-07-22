/**
 * Leetcode
 * problem: 113
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
 * use dfs algorithm
 * pass parameter TreeNode, sum value, list of binaries
 * if sum == targetSum add result
 */
class Solution {
    List<List<Integer>> result;

    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        // 1. init result
        result = new ArrayList<List<Integer>>();
        List<Integer> list = new ArrayList<Integer>();
        helper(root, list, 0, targetSum);
        return result;
    }

    // 2. method for dfs
    private void helper(TreeNode node, List<Integer> list, int sum,int targetSum){
        if(node == null) return;

        sum += node.val;
        list.add(node.val);

        if(node.left == null && node.right == null){
            if(sum == targetSum)result.add(new ArrayList(list));
        }

        helper(node.left, list, sum, targetSum);
        helper(node.right, list, sum, targetSum);

        list.remove(list.size()-1);
    }
}
