# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        temp = []
        def traverse(root: Optional[TreeNode]):
            if not root:
                return
            
            if not root.left and not root.right:
                temp.append(str(root.val))
                result.append("->".join(temp))
                temp.pop()
                return
            
            
            temp.append(str(root.val))
            print(temp)
            traverse(root.left)
            traverse(root.right)
            
            temp.pop()

            
            
        traverse(root)
        return result