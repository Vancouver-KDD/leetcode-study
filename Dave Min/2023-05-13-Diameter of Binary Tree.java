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
    int max;
    public int diameterOfBinaryTree(TreeNode root) {
        max =0;
        longestPath(root);
        return max;        
    }
    public int longestPath(TreeNode node){
        if(node == null) return 0;
        int leftLen = longestPath(node.left); 
        int rightLen = longestPath(node.right);
        max = Math.max(max, leftLen+rightLen);
        return (leftLen > rightLen ? leftLen : rightLen) + 1;
    }
}
//TC: O(N)
//SC: O(N) (if the tree is balanced then it's log N)
