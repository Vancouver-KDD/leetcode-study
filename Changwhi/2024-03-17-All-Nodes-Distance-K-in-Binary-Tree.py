# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # BFS
        # mark every level 
        # below the target node 
            # level of target node + k distance = nodes we want to find
        # above the target node
            # level of target node - k distance = nodes we want to find
        # oppsite side
            # if level of target node - k is negative integer, then k + negative integer = ndoes that we want to find in the opposite side.
        
        # Or 
        # You can traverse from target node. But there is no way to go back upwards.
        # So we can add parent property in an each node
        
        
        def addParent(node, parent):
            if not node:
                return
            node.parent = parent
            addParent(node.left, node)
            addParent(node.right, node)
            
        addParent(root, None) #add parent node starting from the root
        ans = []
        seen = set() # since subtree contains parent node, we should have this to avoid traversing more than once. 
        
        def trav(node, level):
            if not node or node in seen or level > k: #base
                return
            seen.add(node) #To avoid traversing more than once esepcially parent node. 
            if level == k: 
                ans.append(node.val)
                return
            if level+1 <= k:
                trav(node.parent, level+1)
                trav(node.left, level+1)
                trav(node.right, level+1)
        
        trav(target, 0) # traverse from target. since we added parent node in each node, we can go back upwords.
        return ans
    
    