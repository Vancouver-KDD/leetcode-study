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

class BinaryTreeLevelOrderTraversal {
    public List<List<Integer>> levelOrder(TreeNode root) {
        
        // Initialize a queue for BFS traversal
        Queue<TreeNode> queue = new LinkedList<TreeNode>();

        // This will store the final result: a list of levels
        List<List<Integer>> result = new ArrayList<>();

        // If the tree is empty, return an empty list
        if (root == null) return result;
        else queue.add(root);  // Add the root node to start BFS

        // Continue while there are nodes to process
        while (!queue.isEmpty()) {
            int size = queue.size();  // Number of nodes at the current level
            List<Integer> level = new ArrayList<>();  // List to store current level values

            // Process all nodes at this level
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();  // Remove node from the front of the queue
                level.add(node.val);  // Add the node's value to the current level list

                // Add child nodes to the queue for the next level
                if (node.left != null) queue.add(node.left);
                if (node.right != null) queue.add(node.right);
            }

            // After processing the level, add it to the result
            result.add(level);
        }

        // Return the list of levels
        return result;
    }
}
