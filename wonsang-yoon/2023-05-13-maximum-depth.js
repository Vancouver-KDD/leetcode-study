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
    if(root === null){return 0}
    let count_r;
    let count_l;
    //declare right and left nodes
    count_r = maxDepth(root.right)
    count_l = maxDepth(root.left)
    //Math.max can be used to find maximum depth of binary tree and add 1 for current node
    return (Math.max(count_r,count_l))+1;
    
};