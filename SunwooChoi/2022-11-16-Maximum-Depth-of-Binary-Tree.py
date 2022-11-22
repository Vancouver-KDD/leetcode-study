# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.get_depth(root, 0)

    # dfs to get maximum depth of tree
    def get_depth(self, node: TreeNode, cur_depth) -> int:
        if not node:
            return cur_depth
        
        return max(self.get_depth(node.left, cur_depth+1), self.get_depth(node.right, cur_depth+1))

