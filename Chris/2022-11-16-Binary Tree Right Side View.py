# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        index = 0
        
        def addRightSideNode(node, curDepth):
            
            # if the current depth >= current index,
            # add current value to the res
            if node == None:
                return
            
            nonlocal index
            
            if curDepth == index:
                res.append(node.val)
                index += 1
            
            # call right node first then left node
            
            addRightSideNode(node.right, curDepth+1)
            addRightSideNode(node.left, curDepth+1)
        
        addRightSideNode(root, 0)
        
        return res