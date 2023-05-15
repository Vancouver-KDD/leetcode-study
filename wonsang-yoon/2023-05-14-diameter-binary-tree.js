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
    if (root === null)
        return 0;
    let tree_dia = 0;
    dfs(root);


    function dfs(root) {
        if (!root) { return 0 }
        let l_node = 0, r_node = 0;
        if (root.right !== null) {
            r_node = dfs(root.right);
        }
        if (root.left !== null) {
            l_node = dfs(root.left);
        }
        tree_dia = Math.max(tree_dia, r_node + l_node)
        
        return Math.max(r_node, l_node) + 1
    }

    return tree_dia;
};