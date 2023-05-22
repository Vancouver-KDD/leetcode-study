# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        #sol 1 with recursion
        # base case
        if not root:
            return 0

        # 1 bc there's always one root in this case
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
# T O(n)
# S O(n)
