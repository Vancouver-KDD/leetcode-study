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
var invertTree = function (root) {
    //Logic: iterate Binrary tree using recursion and swap right node and left node to make array inverted
    if(root === null){return root}

    //swapping process
    let tempNode = root.right;
    root.right = root.left;
    root.left = tempNode;

    //iterate right side and if root faces nothing on ride try left after
    if(root.right){invertTree(root.right)}
    if(root.left){invertTree(root.left)}
    return root
};
