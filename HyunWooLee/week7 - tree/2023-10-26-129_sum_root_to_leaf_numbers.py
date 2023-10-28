# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 0)])
        num = 0

        while queue:
            node, curr_sum = queue.popleft()
            curr_sum *= 10
            curr_sum += node.val
            if node.left:
                queue.append((node.left, curr_sum))
            if node.right:
                queue.append((node.right, curr_sum))

            if not node.left and not node.right:
                num += curr_sum

        return num

    def sumNumbersDFS(self, root: Optional[TreeNode]) -> int:

        def dfs(root, num):
            if not root:
                return 0

            num *= 10
            num += root.val

            if not root.left and not root.right:
                return num
            return dfs(root.left, num) + dfs(root.right, num)

        return dfs(root, 0)