# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs(root, subRoot)
    
    def dfs(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        result = False
        if not root:
            return False
        if not subRoot:
            return False
        # if find the starting point, compare trees
        if root.val == subRoot.val:
            result = result or self.compareTrees(root, subRoot)
        
        # find the subtree has same strucuture
        result = result or self.dfs(root.left, subRoot)
        result = result or self.dfs(root.right, subRoot)
        
        return result
    
    # compare two tree are same structure
    def compareTrees(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root and subRoot:
            return False
        if root and not subRoot:
            return False
        if root.val != subRoot.val:
            return False
        else:
            return self.compareTrees(root.left, subRoot.left) and self.compareTrees(root.right, subRoot.right)

