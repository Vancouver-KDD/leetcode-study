"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Input: root = [2,1,3]
Output: true

Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
The number of nodes in the tree is in the range [1, 104].
-2^31 <= Node.val <= 2^31 - 1
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        output = []
        self.inorder(root, output)

        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False
        return True

    def inorder(self, root, output):
        if not root:
            return

        self.inorder(root.left, output)
        output.append(root.val)
        self.inorder(root.right, output)

    def isValidBST(self, root):
        def valid(node, left, right):
            if not node:
                return True
            if not (right > node.val > left):
                return False
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        return valid(root, float('-inf'), float('inf'))