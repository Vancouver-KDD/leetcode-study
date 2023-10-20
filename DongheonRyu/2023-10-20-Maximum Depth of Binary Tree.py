def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))


def maxDepth(root):
      if not root:
            return 0
      
      level = 0
      q = deque([root])
      while q:
            
            for i in range(len(q)):
                  node = q.popleft()
                  if node.left:
                        q.append(node.left)
                  if node.right:
                        q.append(node.right)
            level += 1    