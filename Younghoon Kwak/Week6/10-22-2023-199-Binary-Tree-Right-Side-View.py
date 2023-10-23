# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        q=deque([[root,0]])
        d={}
        #print(q)
        while q:
            l = len(q)
            node,line=q.popleft()
            d[line]=node.val
            if node.left:
                q.append([node.left,line+1])
            if node.right:
                q.append([node.right,line+1])
        ans=[]
        for k in sorted(d):
            ans.append(d[k])
        return ans