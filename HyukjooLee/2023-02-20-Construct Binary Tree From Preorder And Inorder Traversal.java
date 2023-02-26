// Given two integer arrays preorder and inorder 
// where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree,
// construct and return the binary tree.
// preorder is guaranteed to be the preorder traversal of the tree.
// inorder is guaranteed to be the inorder traversal of the tree.


// 주어진 preorder tree 의 맨 처음 index (preorder[0]) root 를 기준으로 해서 
// inorder 어레이에서 root 기준 왼쪽 elements 들은 left subtree 가 되고 
// 오른쪽 elements 들은 rifht subtree 가 된다는 것울 유추 할 수 있음

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

// by recursively constructing the left and right subtrees of each node in the binary tree
// inorder traversal: left -> root -> right
// preorder taversal: root -> left -> right
// 1. create a root node with the value of the first element in the preorder array
// 2. find the index of the root node value in the inorder array
// 3. create the left subtree by recursively calling the algorithm
// with the left portion of the inorder array and the same number of elements in the preorder array starting from the second element
// 4. create the right subtree by recursively calling the algorithm 
// with the right portion of the inorder array and the same number of elements in the preorder array starting from
// the index of the root node value in the inorder array plus one.
class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // check if the given preorder or inorder array is empty, there is no tree to build
        if(preorder.length == 0 || inorder.length == 0) return null;
        // call a helper function with start index / end index
        // to keep track of the indexes of the left and right portions,
        // we need to pass the starting and ending indexes of the current subtree's portion
        // as we recursively build the left and right subtrees
        return helperFunction(preorder, inorder, 0, 0, inorder.length - 1);   
    }

    private TreeNode helperFunction(int[] preorder, int[] inorder,  int preStart, int start, int end) {
        TreeNode root = new TreeNode(preorder[preStart]);
        int rootIdx = 0;

        for(int i = start; i < end; i++) {
            if(inorder[i] == root.val) {
                rootIdx = i;
                break;
            }
        }

        root.left = helperFunction(preorder, inorer, preStart +1, start, rootIdx - 1);
        root.right = buildTreeHelper(preorder, inorder, preStart + rootIdx - start + 1, rootIdx + 1, end);
        return root;
    }
}