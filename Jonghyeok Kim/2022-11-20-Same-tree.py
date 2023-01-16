# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         if not p and not q:
#             return True
#         if bool(not q) ^ bool(not p):
#             return False
        
#         q1 = collections.deque([(p, 0)])
#         q2 = collections.deque([(q, 0)])
        
#         while q1 or q2:
#             if bool(not q1) ^ bool(not q2):
#                 return False
#             node1, loc1 = q1.pop()
#             node2, loc2 = q2.pop()
#             if node1.val != node2.val or loc1 != loc2:
#                 return False
#             if node1.left:
#                 q1.append((node1.left,1))
#             if node2.left:
#                 q2.append((node2.left, 1))
#             if node1.right:
#                 q1.append((node1.right, 2))
#             if node2.right:
#                 q2.append((node2.right, 2))
#         return True

        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))