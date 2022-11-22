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

var maxDepth = function(root) {
    return traverse(root, 0);
};

function traverse(root, cnt){
    if(!root) return cnt;
    return Math.max(traverse(root.left, cnt+1), traverse(root.right, cnt+1))
}

