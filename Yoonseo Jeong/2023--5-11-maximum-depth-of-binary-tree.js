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
    if(!root) return 0

    // -- Initial thought
    // to cound number of nodes is (2^h - 1)
    // so to get the depth, 
    // get length of root + 1 / 2

    // -- trying to get the length while going through all nodes using recursion
    // but actually got depth of the tree

    // initial depth
    let depth = 1

    // go through all the node
    const getLength = (node, depthCount) => {
        // if node is null, don't do anything
        if(!node) {
            return
        }
        // if depth count parameter is bigger than depth, assign depthCount to depth
        // if they are same or smaller, don't do anything
        // cause if it went though left and the depth was 3,
        // and now going through right, but it can be shorter than left side
        if(depthCount > depth) depth = depthCount
        // if the node has 1 or 2 child, do recurtion
        if(node.left || node.right) {
            // everytime going to child node, increase the depth count
            getLength(node.left, depthCount+1)
            getLength(node.right, depthCount+1)
        }
    }

    // call the function
    getLength(root, depth)
    
    return depth

    // complexity
    // time: O(n)
    // space: O(n) -> function calls will be placed on the stack
};