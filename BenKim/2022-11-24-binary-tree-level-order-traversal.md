# 102. Binary Tree Level Order Traversal

> Problem link: https://leetcode.com/problems/binary-tree-level-order-traversal/  
> Submission detail: https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/848877222/  


```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # queue를 이용해 BFS를 수행한다
        # for문에서 len(q)가 같은 레벨의 요소들만 pop할수 있도록 해준다

        if not root:
            return []

        result = []
        q = deque([root])
        
        while q:
            same_depth_val = []
            for i in range(len(q)):
                node = q.popleft()
                same_depth_val.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            result.append(same_depth_val)
        
        return result
```