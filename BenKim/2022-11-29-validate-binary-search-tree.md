# 98. Validate Binary Search Tree

> Problem link: https://leetcode.com/problems/validate-binary-search-tree/  
> Submission detail: https://leetcode.com/problems/validate-binary-search-tree/submissions/851657870/  

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # root.left.val < root.val
        # root.righ.val > root.val
        left = float('-inf')
        right = float('inf')
        
        def isValid(node, left, right):
            # 마지막 node에 무사히 도달하게되면 True
            if not node: return True
            # True인 케이스는 내부에서 return을 해, 아래의 False에 도달하지 않게한다
            if node.val < right and node.val > left:
                return (isValid(node.left, left, node.val) and 
                        isValid(node.right, node.val, right))
            # False인 케이스
            return False

        return isValid(root, left, right)
```