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
    /**
        Time Complexity: O(n^2)
            - finding root index in inorder takes O(n) for each recursive call
        Space Complexity: O(1)

        1) The first value of the preorder array is the root of the tree.
        2) The second value of the preorder array is the root of the left sub tree
        3) All values on the left side of the inorder from root are the nodes of the left subtree
        4) All values on the right side of the inorder from root are the nodes of the right subtree
     */
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder.length == 0 || inorder.length == 0) return null;

        TreeNode root = new TreeNode(preorder[0]);
        Integer mid = null;

        for (int i = 0; i < inorder.length; i++) {
            if (root.val == inorder[i]) mid = i;
        }

        if (mid == null) return null;

        root.left = buildTree(Arrays.copyOfRange(preorder, 1, mid + 1), Arrays.copyOfRange(inorder, 0, mid));
        root.right = buildTree(Arrays.copyOfRange(preorder, mid + 1, preorder.length), Arrays.copyOfRange(inorder, mid + 1, inorder.length));

        return root;
    }
}