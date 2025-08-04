# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        longest_diameter = [0]

        def dfs(curr):
            if curr is None:
                return 0

            left_height = dfs(curr.left)
            right_height = dfs(curr.right)
            curr_diameter = left_height + right_height

            longest_diameter[0] = max(longest_diameter[0], curr_diameter)

            return 1 + max(left_height, right_height)

        dfs(root)
        return longest_diameter[0]


solution = Solution()
print(solution.diameterOfBinaryTree(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)),
      TreeNode(3))))
