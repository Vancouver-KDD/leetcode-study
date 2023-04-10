// 100. Same Tree
// Given the roots of two binary trees p and q, write a function to check if they are the same or not.

// Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.


/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
 var isSameTree = function(p, q) {
    if (!p && !q) return true; 
    if (!p || !q) return false;
    return p.val === q.val
        && isSameTree(p.left, q.left)
        && isSameTree(p.right, q.right);
};

//Time Complexity : O(N)
//Space Complexity : O(1)
//DFS Recursion
