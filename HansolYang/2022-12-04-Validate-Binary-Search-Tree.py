# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root or (not root.left and not root.right):
            return True
        
        to_check = deque()
        if root.left:
            to_check.append((root.left, -float(inf), root.val))
        if root.right:
            to_check.append((root.right, root.val, float(inf)))
        
        while to_check:
            curr = to_check.popleft()
            if curr[1] < curr[0].val < curr[2]:
                if curr[0].left:
                    to_check.append((curr[0].left, curr[1], min(curr[0].val, curr[2])))
                if curr[0].right:
                    to_check.append((curr[0].right, max(curr[0].val, curr[1]), curr[2]))
            else:
                return False
            
        return True
            