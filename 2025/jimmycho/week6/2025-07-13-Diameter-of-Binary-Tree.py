# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        def measureDiameter(node):
            nonlocal max_diameter
            if not node:
                return 0
            left = measureDiameter(node.left)
            right = measureDiameter(node.right)
            max_diameter = max(max_diameter, left + right)
            return 1 + max(left, right)
        measureDiameter(root)
        return max_diameter