class Solution {
    int path = 0;
      private int helper(TreeNode node) {
        if (node == null) return 0;
        int leftHeight = helper(node.left);
        int rightHeight = helper(node.right);

        if (leftHeight + rightHeight > path) {
            path = leftHeight + rightHeight;
        }
        return 1 + Math.max(leftHeight , rightHeight);

    }

    public int diameterOfBinaryTree(TreeNode root) {
        helper(root);
        return path;
        
    }
}