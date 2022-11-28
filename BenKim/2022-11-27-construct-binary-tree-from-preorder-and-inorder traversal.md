# 105. Construct Binary Tree from Preorder and Inorder Traversal

> Problem link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/  
> Submission detail: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/850952539/  

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        # preorder: root -> left -> right
        # in order: left -> root -> right
        root = TreeNode()
        root.val = preorder[0]
        mid = inorder.index(preorder[0])

        # left에는 mid의 숫자만큼의 노드들이 있다. preorder의 첫번째 요소 이후 mid만큼의 node가 left에 속한다
        root.left = self.buildTree(preorder[1:mid +1], inorder[:mid])
        root.right = self.buildTree(preorder[mid +1:], inorder[mid + 1:])

        return root
```