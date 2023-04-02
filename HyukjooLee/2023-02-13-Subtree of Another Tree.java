// Given the roots of two binary trees root and subRoot, 
// return true if there is a subtree of root with the same structure
// and node values of subRoot and false otherwise.

// 바이너리 트리와 섭트리가 input 으로 주어지고
// 같은 구조와 같은 value 를 가지고 있는지 체크

// A subtree of a binary tree tree is a tree that 
// consists of a node in tree and all of this node's descendants. 
// The tree tree could also be considered as a subtree of itself.


// we need to check if there is a subtree in the "tree rooted at root"
// == "tree rooted at subRoot"

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
 
// 1. using DFS
// we will use the two functions,
// 1) isSubtree function will ckeck if both the root and the subRoot are null, return true
// if root is null or subroot is null, return false
// if root value is equal to subroot valie, we will check if the two tree are same
// if the values are not same, we will ceck the left and right subtrees of the root to wsee if there is another match
// another function will check if two trees are identical by comparing their node vals an recursively checking their left and right subtrees
// time complexitiy is O(N * M); n is the number of nodes in the root tree, m is the number of subtree
// in the worst case, we have to traverse the entire root tree for each node.. to find a match
// space complexity is O(N); lets say O(H); h is the height of the taller tree; call stack at any time = the height of the taller tree
class Solution {
 public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if(root == null && subRoot == null) return true;
        if(root == null || subRoot == null) return false;
        if(root.val == subRoot.val && areSameSubTree(root, subRoot)) return true;

        return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
    }

    private boolean areSameSubTree(TreeNode root, TreeNode subRoot) {
        if(root == null && subRoot == null) return true;
        if(root == null || subRoot == null) return false;
        if(root.val != subRoot.val) return false;

        return areSameSubTree(root.left, subRoot.left) && areSameSubTree(root.right, subRoot.right);
    }
}

// 2. using pre-order traversal
// check to see if the subRoot tree is a substring of the pre-order representation of the root tree
// time complexity is O(N + M) as we traverse each tree once in order to build the pre-order representation
// space complexity is O(N + M) as we use two strings; each string take up to O(N) the number of nodes in the root & sub
class Solution {    
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        StringBuilder rootSb = new StringBuilder();
        StringBuilder subRootSb = new StringBuilder();

        buildPreOrderStr(root, rootSb);
        buildPreOrderStr(subRoot, subRootSb);
        return rootSb.toString().contains(subRootSb.toString());
    }

    private void buildPreOrderStr(TreeNode root, StringBuilder sb) {
        if(root == null) {
            sb.append(",null");
            return;
        }
        sb.append("," + root.val);
        buildPreOrderStr(root.left, sb);
        buildPreOrderStr(root.right, sb);
    }
}