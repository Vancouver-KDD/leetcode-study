/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} list1
 * @param {TreeNode} list2
 * @return {boolean}
 */
var isSameTree = function (list1, list2) {
    if (!list1 || !list2) { return false }

    if (list1.val !== list2.val) {
        console.log(list1.val, list2.val, 'not same');
        return false;
    }else{
        console.log(list1.val, list2.val,'same');
    }
    if (list1.right && list2.right) {
        isSameTree(list1.right, list2.right)
    }
    if (list1.left && list2.left) {
        isSameTree(list1.left, list2.left)
    }
    if (((!list1.left && list2.left) || (list1.left == !list2.left)) ||
        ((!list1.right && list2.right) || (list1.right == !list2.right))) {
        return false;
    }

    return true
};