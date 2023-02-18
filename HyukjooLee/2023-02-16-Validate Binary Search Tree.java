// Given the root of a binary tree, determine if it is a valid binary search tree (BST).

// A valid BST is defined as follows:

// - The left of a node contains only nodes with keys less than the node's key.
// - The right subtree of a node contains only nodes with keys greater than the node's key.
// - Both the left and right subtrees must also be binary search trees.

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

// 1. using in-order traversal with recursion
// we will check if a tree is a valid binary search tree by performing an inorder traversal

// to be a valid binary tree,
// the left subtree of any node should contain values less than the current
// the right subtree of any node should contain values greater than the current

// if the values are in ascending order, the given tree is valid, otherwise false
// visit left subtree, current, right subtree

// time complexity is O(N) - the number of nodes as we visit each node once
// space complexity is O(N) - array list to store the in-order traversal of the binary tree
class Solution {
    public boolean isValidBST(TreeNode root) {
        List<Integer> inOrder = new ArrayList<>();
        inOrderTraversal(root, inOrder);    
        // check if each value is less than the next value
        for(int i = 0; i < inOrder.size() - 1; i++) {
            if(inOrder.get(i) >= inOrder.get(i + 1)) return false;
        }
        
        return true;
    }

    // a helper function that adds each node values to an ArrayList in ascending order.
    private void inOrderTraversal(TreeNode node, List<Integer> inOrder) {
        if(node == null) return;
        // left , root, right
        inOrderTraversal(node.left, inOrder);
        inOrder.add(node.val);
        inOrderTraversal(node.right, inOrder);
        
    }
}

// 2. using in-order traversal without recursion
// using a stack to keep track of the nodes we will visit
// push the root node onto the stack
// pop the root node from the stack and check if its value is greater than the left first
// update the target node to be the current node
// and push the right child onto the stack

// time complexity is O(N) - the number of nodes as we visit each node once
// space complexity is O(H) - the height of the binary tree; stored onto stack 
class Solution {
    public boolean isValidBST(TreeNode root) {
        Stack<TreeNode> stack = new Stack<>();
        TreeNode current = root;
        TreeNode target = null;

        while(current != null || !stack.isEmpty()) {
            while(current != null) {
                stack.push(current);
                current = current.left;
            }

            current = stack.pop();
            if(target != null && current.val <= target.val) return false;

            target = current;
            current = current.right;
        }

        return true;
    }
}