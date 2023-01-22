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
 //2022-11-29
 //Time Complexity: O(N + K)
 //Space Complexity: O(N)
class Solution {
    public int kthSmallest(TreeNode root, int k) {
        if(root == null || k < 1){
            return -1;
        }

        Stack<TreeNode> stack = new Stack<>();
        int count = 0;
        while(!stack.isEmpty() || root != null){
            if(root != null){
                stack.push(root);
                root = root.left;
            }else{
                TreeNode node = stack.pop();
                count++;
                if(count == k){
                    return node.val;
                }
                root = node.right;
            }
        }
        return -1;
    }
}