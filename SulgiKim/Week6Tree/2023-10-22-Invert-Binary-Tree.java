/*
 * https://leetcode.com/problems/invert-binary-tree/
 * 
 * ## Description
 * Given the root of a binary tree, invert the tree, and return its root.
 * 
 * ## Example
 * Input: root = [4,2,7,1,3,6,9], Output: [4,7,2,9,6,3,1]
 */
class Solution {
    public TreeNode invertTree(TreeNode root) {
        //Set the early exit 
        if(root == null) return null;
				
		//recursive call
        TreeNode left = invertTree(root.left);
        TreeNode right = invertTree(root.right);
				
		//swapping the children
        root.left = right;
        root.right = left; 

        return root; 
    }
}