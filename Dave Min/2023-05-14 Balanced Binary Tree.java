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
    boolean result;
    public boolean isBalanced(TreeNode root) {
         result = true;
         DoIsBalanced(root,0);
         return result;
    }

    public int DoIsBalanced(TreeNode node,int cnt) {
        if(node==null) return cnt;
        cnt++;
        int left = DoIsBalanced(node.left, cnt);
        int right = DoIsBalanced(node.right, cnt);

        if(Math.abs(left-right) >1) result = false;
        if(!result) return 0;

        return Math.max( left, right);
    }    
}
// TC: O(N);
// SC: O(N);
