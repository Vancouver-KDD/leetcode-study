class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """ 
        if not root:
            return False 
        pathStack_rootToCurrNode = [(root, root.val)]
        
        while pathStack_rootToCurrNode:
            node, val = pathStack_rootToCurrNode.pop() 
            if not node.left and not node.right and val == targetSum:
                return True
            
            if node.left:
                pathStack_rootToCurrNode.append((node.left, val + node.left.val))
            if node.right:
                pathStack_rootToCurrNode.append((node.right, val + node.right.val))
        
        return False    