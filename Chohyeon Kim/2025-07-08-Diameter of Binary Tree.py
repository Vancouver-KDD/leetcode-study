# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max_d = 0

        
        def dfs(node):
            nonlocal max_d

            if not node:
                return 0


            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)

            d = leftHeight + rightHeight

            max_d = max(max_d, d)

            return max(leftHeight, rightHeight) + 1

        dfs(root)

        return max_d