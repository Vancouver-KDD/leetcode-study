class Solution:
    def __init__(self):
        self.diameter = 0
    
    def depth(self, head: Optional[ListNode]) -> int:
        left = self.depth(head.left) if node.left else 0
        right = self.depth(head.right) if node.right else 0

        if left + right > self.diameter:
            self.diameter = left + right
        
        return 1 + (left if left > right else right)
    
    def diameterOfBinaryTree(self, root: Optional[ListNode]) -> int:
        self.depth(root)
        return self.diameter