class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        idx_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def build(in_left: int, in_right: int) -> Optional[TreeNode]:
            if in_left > in_right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            index = idx_map[root_val]
            root.left = build(in_left, index - 1)
            root.right = build(index + 1, in_right)
            return root

        return build(0, len(inorder) - 1)
