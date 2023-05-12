# Given the root of a binary tree, invert the tree, and return its root.

# Constraints:
# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# this question is much easier if done recursively
# 1. define the base cases: if the root is null, return None
# 2. create a temp root to hold one of the children node
# 3. swap the left and right node, using the temp
# 4. consider the left and right nodes to be the root node and feed it back into the function
# 5. return the root once all recursive iterations are complete

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
