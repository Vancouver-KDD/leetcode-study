# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:


        # if root.left is None and root.right is None:
        #     return [str(root.val)]
        # elif root.left is None:
        #     return [str(root.val) + '->' + i for i in self.binaryTreePaths(root.right)]
        # elif root.right is None:
        #     return [str(root.val) + '->' + i for i in self.binaryTreePaths(root.left)]
        # else:
        #     return [str(root.val) + '->' + i for i in self.binaryTreePaths(root.left)] + [str(root.val) + '->' + i for i in self.binaryTreePaths(root.right)]
        def dfs(node, path):
            if node:
                path += str(node.val)
                if not node.left and not node.right:
                    paths.append(path)
                else:
                    path += "->"
                    dfs(node.left, path)
                    dfs(node.right, path)
        paths = []
        dfs(root, "")
        return paths