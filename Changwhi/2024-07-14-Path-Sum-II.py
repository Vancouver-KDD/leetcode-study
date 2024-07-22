# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        temp = []
        def traverse(root, targetSum):
            if not root:
                return
            if not root.left and not root.right:
                temp.append(root.val)
                if sum(temp) == targetSum:
                    result.append(temp[:])  # Append a copy of temp
                temp.pop()
                return
            temp.append(root.val)
            traverse(root.left, targetSum)
            traverse(root.right, targetSum)
            temp.pop()

        traverse(root, targetSum)
        return result