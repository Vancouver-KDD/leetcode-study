class Solution:
    def isBalanced(self, root: Optional[ListNode]) -> bool:
        return (self.get_height(root) >= 0)
    
    def get_height(self, root: Optional[ListNode]) -> bool:
        if root is None: return 0
        leftheight, rightheight = self.get_height(root.left), self.get_height(root.right)
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1: return -1 # 1
        return max(leftheight, rightheight) + 1

# 1. abs() is function to get a absolute value