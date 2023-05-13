# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Constraints:
# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

# 1. use recursive DFS
# 2. define base case, which is if root is null (None in Python), return 0
# 3. else 1 + max of (left node dfs + right node dfs)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))