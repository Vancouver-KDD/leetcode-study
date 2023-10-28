/**
 * Recursive Solution
 * Time Complexity: O(N). Goes through all nodes in tree once.
 * Space Complexity: O(H), where H is the height of the tree. This is to keep recursion stack. 
*/
class Solution {
    int result;
    public int sumNumbers(TreeNode root) {
        result = 0;
        helper(root,result);

        return result;
    }

    public void helper(TreeNode node, int sum) {
        if(node == null) {
            return;
        }

        sum = sum*10 + node.val;

        //if you reach leaf node, add sum to result
        if(node.left == null && node.right == null) {
            result += sum;
            return;
        }

        helper(node.left,sum);
        helper(node.right,sum);
    }
}