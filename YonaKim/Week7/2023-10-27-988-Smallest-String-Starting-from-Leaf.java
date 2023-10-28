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
 * Time Complexity: O(N)
 * Space Complexity: O(N)
 */
class Solution {
    String smallest;
    public String smallestFromLeaf(TreeNode root) {
        //can also use new StringBuilder()
        helper(root,"");

        return smallest;
    }

    public void helper(TreeNode node, String str) {
        if(node == null) {
            return;
        }

        //add char(int to char) to to string
        //need to add 97 or 'a' because char 'a' has a decimal value of 97 in ascii table
        str = Character.toString(node.val + 'a') + str;

        //if reached leaf of tree, compare current string to smallest.
        //if current string is smaller, update smallest
        if(node.left == null && node.right == null) {
            if(smallest == null) {
                smallest = str;
            }
            smallest = smallest.compareTo(str) <= 0 ? smallest : str;
        }

        //recursion
        helper(node.left, str);
        helper(node.right, str);
    }
}