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
var diameterOfBinaryTree = function (root) {
    let max = 0;
    let res = recursive(root);
    return max -1;

    function recursive(root) {
        if (!root) {
            return 0;
        }

        let left = recursive(root.left);
        let right = recursive(root.right);
        let curr = left + right + 1;
        max = Math.max(curr,max);
        curr = Math.max(left, right) + 1;

        return curr;

    }
};
