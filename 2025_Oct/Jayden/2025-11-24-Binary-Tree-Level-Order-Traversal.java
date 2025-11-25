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
        Time Complexity: O(n)
            - where n is the number of nodes in tree, each node is visited only once
        Space Complexity: O(n)
     */
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        Queue<TreeNode> queue = new ArrayDeque<>();

        if (root == null)
            return result;
        queue.offer(root);

        while (!queue.isEmpty()) {
            int numElementsAtCurrentLevel = queue.size();

            List<Integer> currentLevel = new ArrayList<>();

            // adds nodes in current level in list while checking for its child eligibility
            for (int i = 0; i < numElementsAtCurrentLevel; i++) {
                TreeNode node = queue.poll();
                currentLevel.add(node.val);

                if (node.left != null)
                    queue.offer(node.left);
                if (node.right != null)
                    queue.offer(node.right);
            }

            result.add(currentLevel);
        }

        return result;
    }
}