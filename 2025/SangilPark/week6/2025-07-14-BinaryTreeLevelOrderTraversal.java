package week6;
import java.util.*;

/*
 * Week 6: DFS/BFS
 * https://leetcode.com/problems/binary-tree-level-order-traversal/
 */
class Solution {
    public static List<List<Integer>> levelOrder(TreeNode root) {
        // bfs
        // treverse by level (with bfs) left -> right
        // add subList into result
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) return result;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            int size = queue.size();
            List<Integer> subList = new ArrayList<>();
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                subList.add(node.val);

                if (node.left != null) queue.offer(node.left);
                if (node.right != null) queue.offer(node.right);
            }
            result.add(new ArrayList(subList));
        }

        return result;
    }

    public static void main(String[] args) {
        int[] input = {1,2,3,4,5};
        TreeNode head = new TreeNode(1);
        levelOrder(head);
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