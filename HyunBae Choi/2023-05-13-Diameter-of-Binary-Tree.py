# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

# Constraints:
# The number of nodes in the tree is in the range [1, 104].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 0. assign a attribute to keep track of the result
# 1. define a nested dfs function to calculate the height of the left and right tree
# 2. since we want the diameter, update the result by calculating the max between current result and the height of left and right tree combined
# 3. call dfs on root, result results 

class Solution:
    def __init__(self):
            self.result = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if root is None:
                return 0

            height_left = dfs(root.left)
            height_right = dfs(root.right)
            self.result = max(self.result, (height_left + height_right))

            return 1 + max(height_left, height_right)
        
        dfs(root)

        return self.result