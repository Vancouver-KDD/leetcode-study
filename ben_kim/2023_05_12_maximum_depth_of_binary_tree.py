# Recursive
class Solution:
    def maxDepth(self, root: Optional[ListNode]) -> int:
        def dfs(root, depth):
            if not root: return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
        
        return dfs(root, 0)

# BFS
class Solution:
    def maxDepth(self, root: Optional[ListNode]) -> int:
        depth = 0
        if not root:
            return 0
        
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1
        
        return depth
