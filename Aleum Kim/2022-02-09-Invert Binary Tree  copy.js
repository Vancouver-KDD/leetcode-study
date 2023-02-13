/**
 * https://leetcode.com/problems/invert-binary-tree/
 * TIme O(N) | Space O(N)
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = function(root) {

    const reverseNodes = (node) => {
        if(node == null) {
            return;
        }
        reverseNodes(node.left);
        reverseNodes(node.right);
        
        let hold = node.left;
        node.left = node.right;
        node.right = hold
    }
    reverseNodes(root)
    return root;
}

var invertTree = function(root) {
    if (root === null) return null;
    let temp = root.left
    root.left = root.right;
    root.right = temp;

    invertTree(root.left)
    invertTree(root.right)

    return root
}


