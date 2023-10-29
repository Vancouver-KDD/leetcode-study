class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        left_height=self.height(root.left)
        right_height=self.height(root.right)
        
        left_diameter=self.diameterOfBinaryTree(root.left)
        right_diameter=self.diameterOfBinaryTree(root.right)
        
        return max((left_height+right_height), max(left_diameter,right_diameter))
        
    
    def height(self,root):
        if root is None:
            return 0
        
        else:
            left_height=self.height(root.left)
            right_height=self.height(root.right)
        
            return 1 + max(left_height, right_height)