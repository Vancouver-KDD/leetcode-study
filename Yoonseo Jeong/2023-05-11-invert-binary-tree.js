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
 * @return {TreeNode}
 */
var invertTree = function(root) {
    if (!root) return root

    // switch root's left and right
    // var root.left
    // root.left = roo.right
    // root.right = root.left

    // think it should be recursion
    // two step every round
    // go to left first and when they get out of it
    // go to right and switch their child
    // until node does not have any child
    // return root when recursion is done
    
    const temp = root.left
    root.left = root.right
    root.right = temp

    if(root.right || root.left) {
        invertTree(root.left)
        invertTree(root.right)
    }

    return root

    // complexity
    // time: O(n)
    // space: O(n) -> function calls will be placed on the stack
};

// Iterative한 방법도 있는데 진짜 이해안됨
// https://leetcode.com/problems/invert-binary-tree/solutions/399221/clean-javascript-iterative-dfs-bfs-solutions/?languageTags=javascript