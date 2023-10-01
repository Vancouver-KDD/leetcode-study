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
var inorderTraversal = function(root) {
    let arr = [];
    recursive(root,arr);
    return arr;
};

function recursive(root, arr){
    if(root){
        recursive(root.left, arr);
        arr.push(root.val);
        recursive(root.right, arr);
    }
}