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
var sumNumbers = function (root) {
    if (!root) {
        return 0;
    }
    let res = 0;
    recursive(root, 0);

    return res;

    function recursive(root, sum) {
        if (root) {
            sum *= 10;
            sum += root.val;

            if (!root.left && !root.right) {
                res += sum;
            } else {
                recursive(root.left, sum);
                recursive(root.right, sum);
            }
        }
    }
};
