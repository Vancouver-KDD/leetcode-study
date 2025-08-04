# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root) -> int:
        if root is None:
            return 0

        def dfs(curr, count):
            if curr is None:
                return count

            if not curr.left and not curr.right:
                return count

            count += 1

            return max(dfs(curr.left, count), dfs(curr.right, count))

        return dfs(root, 1)


solution=Solution()
print(solution.maxDepth(TreeNode(0)))
print(solution.maxDepth(TreeNode(3, TreeNode(9, None, None), TreeNode(20, TreeNode(15), TreeNode(7)))))
