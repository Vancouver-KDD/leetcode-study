// Given the root of a binary search tree, and an integer k,
// return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

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

// 1. using a stack to keep track of the nodes to be visited
// push all left children of the root node onto the stack
// then loop until the stack is empty
// or til we found the Kth smallest value

// pop the top node from the stack
// and decrement the value of k
// when k reaches 0, then we found the Kth smallest value

// otherwise, we continue our traversal by visiting the right child

// time complexity is O(H); maximum number of nodes in the stack = height of the tree
// space complexity is same 
class Solution {
    public int kthSmallest(TreeNode root, int k) {
        Stack<TreeNode> stack = new Stack<>();
        TreeNode current = root;

        while(current != null || !stack.isEmpty()) {
            while(current != null) {
                stack.push(current);
                current = current.left;
            }

            current = stack.pop();
            if(--k == 0) return current.val;

            current = current.right;
        }
        return -1;
    }
}