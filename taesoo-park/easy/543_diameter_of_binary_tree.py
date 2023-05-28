class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.get_height(root)
        return self.diameter
        
    def get_height(self, node):
        if not node:
            return 0
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        self.diameter = max(self.diameter, left_height + right_height)
        return max(left_height, right_height) + 1