class Solution:
    def invertTree(self, root: Optional[ListNode]) -> Optional[ListNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left # 1

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# 1. Same as below
# temp = root.left
# root.left = root.right
# root.right = temp