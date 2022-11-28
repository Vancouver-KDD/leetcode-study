# 226. Invert Binary Tree

> Problem link: https://leetcode.com/problems/invert-binary-tree/  
> submission detail: https://leetcode.com/problems/invert-binary-tree/submissions/848471410/  

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left);
        self.invertTree(root.right);

        return root
```