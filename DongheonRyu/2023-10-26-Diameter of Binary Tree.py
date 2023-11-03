def diameterOfBinaryTree(self, root):
        def dfs(node):
            if not node:
                return 0
            
            # Recursively find the depths of the left and right subtrees
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            
            # Update the diameter if the path through the current node is the longest
            self.diameter = max(self.diameter, left_depth + right_depth)
            
            # Return the depth of the current node
            return 1 + max(left_depth, right_depth)
        
        self.diameter = 0  # Initialize diameter to 0
        dfs(root)  # Start the DFS from the root
        return self.diameter




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # if no root => return None
    # is left or right?
    # if true count++
    # else max prev,curr
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
 
        if not root:
            return 0

        stack = [(root, False)]
        depths = {}
        max_diameter = 0

        while stack:
            node, visited = stack.pop()

            if node:
                if not visited:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
                else:
                    left_depth = depths.get(node.left, -1)
                    right_depth = depths.get(node.right, -1)
                    depths[node] = 1 + max(left_depth, right_depth)
                    max_diameter = max(max_diameter, left_depth + right_depth + 2)

        return max_diameter