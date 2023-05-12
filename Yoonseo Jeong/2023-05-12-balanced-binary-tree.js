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
 * @return {boolean}
 */
var isBalanced = function(root) {
    if (!root) return true

    const check = (node) => {
        if (!node) return 0;
        let left = 1 + check(node.left);
        let right = 1 + check(node.right);
        if (Math.abs(left - right) > 1) return Infinity;
        return Math.max(left, right);
    }

    return check(root)==Infinity?false:true
};

// reference: https://leetcode.com/problems/balanced-binary-tree/solutions/2011001/o-n-time-beats-99-97-memory-speed-0ms-may-2022/?languageTags=javascript