package week6;
import java.util.*;

/*
 * Week 6: DFS/BFS
 * https://leetcode.com/problems/maximum-depth-of-binary-tree/
 */
class Solution {
    public static int maxDepth(TreeNode root) {
        return dfs(root);
    }

    private static int dfs(TreeNode node) {
        // bottom-up
        if (node == null) return 0;     // left node

        int left = dfs(node.left);
        int right = dfs(node.right);

        return 1 + Math.max(left, right);
    }

    public static void main(String[] args) {
        int[] input = {1,2,3,4,5};
        TreeNode head = new TreeNode(1);
        maxDepth(head);
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