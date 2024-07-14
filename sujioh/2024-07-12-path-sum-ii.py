class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(root, targetSum, path):
            if not root:
                return []
            targetSum -= root.val
            path.append(root.val)
            if not root.left and not root.right:  # Is leaf node
                if targetSum == 0:  # Found a valid path
                    ans.append(path.copy())
            else:
                dfs(root.left, targetSum, path)
                dfs(root.right, targetSum, path)
            path.pop()  # backtrack

        ans = []
        dfs(root, targetSum, [])
        return ans