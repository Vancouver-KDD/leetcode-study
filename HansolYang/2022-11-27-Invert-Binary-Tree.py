# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return root
        
        todo = deque()
        p = root
        todo.append((p, p.left, p.right))
        
        while todo:
            curr = todo.popleft()
            p, l, r = curr[0], curr[1], curr[2]
            
            p.left = r
            p.right = l
            
            if l:
                todo.append((l, l.left, l.right))
            if r:
                todo.append((r, r.left, r.right))
                
        return root
            