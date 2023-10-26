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