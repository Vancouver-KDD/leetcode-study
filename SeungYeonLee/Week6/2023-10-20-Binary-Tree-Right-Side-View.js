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
 * @return {number[]}
 */
var rightSideView = function (root) {
    if (!root) {
        return [];
    }
    let res = [];
    recursive(root, 0);
    return res;

    function recursive(n, index) {
        if (!n) {
            return;
        }
        res[index] = n.val;
        recursive(n.left, index + 1);
        recursive(n.right, index + 1);
    }
};
