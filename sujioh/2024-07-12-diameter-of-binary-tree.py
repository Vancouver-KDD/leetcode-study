class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        
        def postOrder(p):
            if not p: return 0
            left, right = postOrder(p.left), postOrder(p.right)
            self.ans = max(self.ans, left+right)
            return 1 + max(left, right)
            
        postOrder(root)
        return self.ans