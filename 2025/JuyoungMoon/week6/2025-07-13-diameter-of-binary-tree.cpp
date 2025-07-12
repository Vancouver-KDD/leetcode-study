// Author: Juyoung Moon

// KDD LeetCode Study Week 6: Trees (DFS/BFS)
// https://github.com/juyomo/leetcode-study

// LeetCode #543.
// https://leetcode.com/problems/diameter-of-binary-tree/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */

function recur(root, depth) {

}

var diameterOfBinaryTree = function(root) {
    if (root == null) {
        return 0;
    }
    
    return recur(root)
};
