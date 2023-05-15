class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if not node:
                return 0
            left_height = height(node.left)
            right_height = height(node.right)
            return 1 + max(left_height, right_height)
        
        def balanced(node):
            if not node:
                return True
            left_height = height(node.left)
            right_height = height(node.right)
            if abs(left_height - right_height) > 1:
                return False
            return balanced(node.left) and balanced(node.right)
        
        return balanced(root)