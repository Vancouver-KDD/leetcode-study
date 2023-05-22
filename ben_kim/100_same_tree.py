class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q: return True # 1
        if not p or not q: return False
        if p.val != q.val: return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# 1. More strict conditions should be checked first.