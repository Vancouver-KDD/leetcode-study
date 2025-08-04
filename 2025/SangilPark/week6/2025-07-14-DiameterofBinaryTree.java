package week6;
import java.util.*;

/*
 * Week 6: DFS/BFS
 * https://leetcode.com/problems/diameter-of-binary-tree/
 */
class Solution {
    static int result = 0;

    public static int diameterOfBinaryTree(TreeNode root) {
        dfs(root);
        return result;
    }

    private static int dfs(TreeNode node) {
        if (node == null) return 0;     // leaf node

        int left = dfs(node.left);
        int right = dfs(node.right);

        result = Math.max(left + right, result);

        return Math.max(left, right) + 1;
    }

    public static void main(String[] args) {
        int[] input = {1,2,3,4,5};
        TreeNode head = new TreeNode(1);
        diameterOfBinaryTree(head);
    }

    public class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode() {}
      TreeNode(int val) { this.val = val; }
      TreeNode(int val, TreeNode left, TreeNode right) {
          this.val = val;
          this.left = left;
          this.right = right;
      }
  }
}