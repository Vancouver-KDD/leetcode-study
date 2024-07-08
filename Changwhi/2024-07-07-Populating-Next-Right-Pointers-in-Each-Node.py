"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque([root] if root else [])
        while q:
            level = []
            for _ in range(len(q)):
                currentNode = q.popleft()
                level.append(currentNode)
                if currentNode.left:
                    q.append(currentNode.left)
                    q.append(currentNode.right)
            for i in range(len(level)):
                level[i].next = level[i+1] if (i < len(level) -1) else None 
        return root
                