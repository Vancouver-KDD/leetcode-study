# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        count=0
        if not root:
            return root
        result = []
        if count == 0:
            self.addFirst(root, result)
        count+=1
        if root.right:
            result.append(root.right.val)
            result += self.rightSideView(root.right)
        result = list(dict.fromkeys(result))

        return result
    
    def addFirst(self, root, result):
        result.append(root.val)