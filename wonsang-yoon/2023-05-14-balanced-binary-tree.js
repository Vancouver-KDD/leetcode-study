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

/*
    Logic: find maximum height of the left and rigt node
    check the difference between left and right height
    if the difference is over 1, return false which is not balanced tree

*/
var isBalanced = function(root) {
    if(root === null) {return true}
    let l_node, r_node;
    //Find node Heights
    l_node = dfs(root.left);
    r_node = dfs(root.right);

    //Find Left and Right node difference
    if(Math.abs(l_node - r_node) > 1)
        return false;
    else
        return true
};
const dfs = (root) =>{
    if(!root){return 0}
    //add one every connection
    return 1+ Math.max(dfs(root.right),dfs(root.left))
}