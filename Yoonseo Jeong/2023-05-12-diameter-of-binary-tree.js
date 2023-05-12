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
var diameterOfBinaryTree = function(root) {
    if (!root) return 0

    // need find most left node and most right node
    // get depth of left and right side and sum

    let diameter = 0

    const check = (node) => {
        // return 0 if node is null
        if(!node) return 0
        
        // recursively call check function on left and right
        let left = check(node.left)
        let right = check(node.right)

        // getting larger number
        diameter = Math.max(diameter, left + right)

        // return larger number + 1 (more depth side)
        return Math.max(left, right) + 1
    }

    // call the function
    check(root)

    return diameter

    // complexity
    // time: O(n)
    // space: O(n)
};

// reference: https://leetcode.com/problems/diameter-of-binary-tree/solutions/3170066/js-recursion-dfs/?languageTags=javascript