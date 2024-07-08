/**
 * Leetcode
 * problem: 103
 * link: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
 * tag: Tree, Breadth-First Search, Binary Tree
 */

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
    private List<List<Integer>> result;

    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        result = new ArrayList();
        helper(root,0);
        for(int i = 0; i < result.size();i++){
            if(i%2 == 1) Collections.reverse(result.get(i));
        }
        return result;
    }

    private void helper(TreeNode node,int idx){
        if(node == null) return;
        if(result.size() <= idx) result.add(new ArrayList());
        result.get(idx).add(node.val);
        helper(node.left, idx+1);
        helper(node.right, idx+1);
    }
}