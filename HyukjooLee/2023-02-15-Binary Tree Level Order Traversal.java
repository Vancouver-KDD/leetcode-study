// Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

// Breath-Depth-Search
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

// 1. iteration - using a queue structure to perform a level-order traversal in a tree
// we start by adding the root to the queue, and loop until the queue is empty
// in each iteration, we will determine the size of the queue = the number of nodes at the current level
// and a list will hold the values and these nodes; we will store the values to the current level list
// by adding their childrent of these nodes to the queue
// finally, add the level list to the result list and jump to the next level
// once we done, return it
// time complexity is O(N) as each loop execute once only
// space complextiy is O(N) as we store the number of nodes in the tree; queue used for the traversal; contains all nodes
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {

        List<List<Integer>> nodesAtLevels = new LinkedList<List<Integer>>();
        // create a queue to store nodes of the tree in a level-order traversal
        Queue<TreeNode> queue = new LinkedList<>();
        
        // check if the root is null, if so return the empty list 
        if(root == null) return nodesAtLevels;

        // add the root to the queue
        queue.offer(root);

        while(!queue.isEmpty()) {
            // queue size; means the number of nodes at the current level
            int size = queue.size();
            // a level list to hold the values of these nodes
            List<Integer> level = new ArrayList<>();
            // traverse the nodes in the queue
            for(int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                // add the value and their children
                level.add(node.val);
                if(node.left != null) queue.offer(node.left);
                if(node.right != null) queue.offer(node.right);
            }
            // add the level list to the result list
            nodesAtLevels.add(level);
        }
        return nodesAtLevels;
    }
}

// 2. using recursion with DFS - Depth-First-Search
// to keep track of the level of each node in the tree, and a list of lists to store
// values of nodes at each level, we add each node's value to the corresponding to its level
// time complexity is O(N); the number of nodes in the tree
// space complexity is O(N); the number of nodes in the tree
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> nodesAtLevels = new LinkedList<List<Integer>>();
        levelOrderHelper(nodesAtLevels, root, 0);
        return nodesAtLevels;
    }

    // helper function that takes the root node, list(result list), the current level as params
    // add the current node's value to its level, calling the function recursively
    // with the left and right children of the current node; incrementing by 1
    private void levelOrderHelper(List<List<Integer>> nodesAtLevels, TreeNode root, int level) {
        if(root == null) return;

        if(level == nodesAtLevels.size()) nodesAtLevels.add(new ArrayList<Integer>());

        nodesAtLevels.get(level).add(root.val);

        levelOrderHelper(nodesAtLevels, root.left, level+1);
        levelOrderHelper(nodesAtLevels, root.right, level+1);
    }
}