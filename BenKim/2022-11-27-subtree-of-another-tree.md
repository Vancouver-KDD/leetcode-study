# 572. Subtree of Another Tree

> Problem link: https://leetcode.com/problems/subtree-of-another-tree/  
> Submission detail: https://leetcode.com/problems/subtree-of-another-tree/submissions/850431319/  

```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # None은 모두의 subtree이다
        if not subRoot: return True

        # root보다 subRoot가 더 많이 있는 경우 sub가 될 수 없다
        if not root and subRoot: return False

        if self.isSameTree(root, subRoot):
            return True

        # 현재 node에서는 같지 않은경우 좌우 브랜치 둘중하나에서라도 나오면 True이다

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))     

    def isSameTree(self, r, t):
        # 최종적으로 둘다 None이면 True
        if not r and not t:
            return True
        
        if r and t and r.val == t.val:
            return self.isSameTree(r.left, t.left) and self.isSameTree(r.right, t.right)

        # 중요한 케이스들을 추리고, 나머지는 else로 한번에 처리한다
        # 둘중 하나가 None인경우, 둘의 val가 다른경우
        return False

```
