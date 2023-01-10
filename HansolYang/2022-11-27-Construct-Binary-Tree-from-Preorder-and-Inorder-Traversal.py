# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:\
        
        hm = {v:i for i, v in enumerate(inorder)}
        index = 0
        
        def DFS(l, r):
            if l > r:
                return None
            nonlocal index
            root_val = preorder[index]
            index += 1
            
            node = TreeNode(root_val)
            node.left = DFS(l, hm[root_val] - 1)
            node.right = DFS(hm[root_val] + 1, r)
            
            return node
        
        root = DFS(0, len(preorder) - 1)
        
        return root
        
        
        
#         def buildNodes(pre, l, r node):
#             if pre == None or len(pre) == 0:
#                 node.left = None
#                 node.right = None
#             else:
#                 node.left = TreeNode(pre.pop(0) if pre != [] else None)
#                 node.right = TreeNode(pre.pop(0) if pre != [] else None)
#                 l -= 1
#                 r = 
#                 buildNodes(pre, l)
        
#         root_p = 0
#         for i in inorder:
#              if i == preorder[0]:
#                 break
#             else:
#                 root_p += 1
#         left = root_p
#         right = root_p
        
#         root = None
        
#         if not preorder:
#             return root
        
       # else:
            
        
        
#         level = 0
#         root_p = 0
#         for i in inorder:
#             if i == preorder[0]:
#                 break
#             else:
#                 root_p += 1
#         left = root_p
#         right = root_p
        
#         res = None
#         if preorder:
#             res = TreeNode(pre)
#             level += 1
#             left -= 1
#             right += 1
        
#         while preorder:
            
#             for _ in range(2**level):
#                 res.append(preorder.pop(0) if left >= 0 else None)
#                 left -= 1
#                 print(res)
            
#             for _ in range(level):
#                 res.append(preorder.pop(0) if right <= len(inorder) else None)
#                 right += 1
#                 print(res)
            
#             level += 1
            
        
#         return res
            

        
                