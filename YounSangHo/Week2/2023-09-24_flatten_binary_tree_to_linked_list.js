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
 * @return {void} Do not return anything, modify root in-place instead.
 */
var flatten = function (root) {
  if (!root) {
    return null;
  }

  let currentNode = root;

  while (currentNode) {
    if (currentNode.left) {
      // Find the rightmost node in the left subtree
      let rightmost = currentNode.left;
      while (rightmost.right) {
        rightmost = rightmost.right;
      }

      // Move the entire right subtree to the rightmost node's right
      rightmost.right = currentNode.right;
      currentNode.right = currentNode.left;
      currentNode.left = null;
    }

    currentNode = currentNode.right;
  }
};

// Helper function to print the flattened tree (linked list)
function printFlattenedList(head) {
  let current = head;
  while (current) {
    console.log(current.val);
    current = current.right;
  }
}
