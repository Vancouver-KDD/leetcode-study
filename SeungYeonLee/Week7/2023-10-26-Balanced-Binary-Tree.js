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
var isBalanced = function (root) {

    let flag = true;
    let l = recursive(root);
    return flag;

    function recursive(root) {
        if (!root) {
            return 0;
        }

        let left = recursive(root.left);
        let right = recursive(root.right);

        if(Math.abs(left - right) > 1){
            flag = false;
        }

        return Math.max(left, right) + 1;
    }
};