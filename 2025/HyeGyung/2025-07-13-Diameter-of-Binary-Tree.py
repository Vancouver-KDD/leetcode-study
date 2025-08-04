# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.diameter = 0 

        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)

            self.diameter = max(self.diameter, left + right)

            return 1 + max(left, right)

        depth(root)
        return self.diameter
