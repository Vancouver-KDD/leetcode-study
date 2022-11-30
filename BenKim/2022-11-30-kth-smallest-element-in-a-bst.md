# 230. Kth Smallest Element in a BST

> Problem link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/  
> Submission detail: 
> - https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/852055230/  
> - https://leetcode.com/problems/kth-smallest-element-in-a-bst/submissions/852070545/

- BST는 inorder로 traversal하면 정렬된 상태가 된다

## brute force
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # 트리내 모든값을 배열에 넣고, 정렬
        res = []

        def searchBST(root):
            if not root: return

            res.append(root.val)
            searchBST(root.left)
            searchBST(root.right)

        searchBST(root)
        res.sort()
        
        return res[k-1]

        
```

## stack iterative
```py
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        curr = root

        while curr or stack:
            # 왼쪽 끝까지 내려간후, 올라온다
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right
        
```