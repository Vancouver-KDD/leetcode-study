# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        in_order = []
        # add node values inorder in the list
        self.bfs(root, in_order)
        # get element in kth smallest value
        return in_order[k-1]
    
    def bfs(self, root, lst):
        if not root:
            return
        self.bfs(root.left, lst)
        lst.append(root.val)
        self.bfs(root.right, lst)

