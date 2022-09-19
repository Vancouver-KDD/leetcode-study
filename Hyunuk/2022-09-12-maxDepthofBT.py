class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(node, depth):
            if not node:
                return depth - 1
            return max(helper(node.left, depth + 1), helper(node.right, depth + 1))
        return helper(root, 1)
