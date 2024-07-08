# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Check left and right if both are there
        # recursion -> the first time meet the condition -> return the node
        res = None

        def find_node(node):
            nonlocal res
            if not node:
                return False
            left_node = find_node(node.left)
            right_node = find_node(node.right)
            this_node = node == p or node == q
            if left_node + right_node + this_node >= 2:
                res = node
            return left_node or right_node or this_node

        find_node(root)

        return res
