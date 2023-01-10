# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        stack = []
        while True:
            
            while root:
                stack.append(root)
                root = root.left
            # decreament k each time you pop meaning u visited the smallest value among the unvisited
            root = stack.pop()
            k -= 1
            
            # when u visit kth smallest value
            if not k:
                return root.val
            
            # in-order traversal : left children - root - right children
            root = root.right
            
            