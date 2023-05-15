# Definition for a binary tree node.
# Given a binary tree, determine if it is height-balanced.
# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

# Constraints:
# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

# 1. recognize that if we do it from top down, we would need to visit nodes we have already visited,
#    meaning it will become O(n) * n, therefore O(n^2)
# 2. implement a dfs funtion to calculate the height of a tree
# 3. settle 3 conditions: 1. the absolute difference of the left and right heights are less than or equal to 1 in the current tree, 2. tree of left node is balanced, 3. tree of right node is balanced
# 4. unless all 3 conditions are satisfied, return False

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def dfs_get_height(root):
            if root is None:
                return 0

            height_left = dfs_get_height(root.left)
            height_right = dfs_get_height(root.right)

            return 1 + max(height_left, height_right)

        height_left = dfs_get_height(root.left)
        height_right = dfs_get_height(root.right)

        if abs(height_left - height_right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
            
        return False
