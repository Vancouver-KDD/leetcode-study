# 235. Lowest Common Ancestor of a Binary Search Tree

> Problem link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/  
> Submission detail: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/852707546/  

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # BST 특성상 q와 q가 left와 right로 쪼개지게 되면 그게 Lowest Common Ancestor이다
        curr = root
        while curr:
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right
            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left
            else:
                return curr
           

```