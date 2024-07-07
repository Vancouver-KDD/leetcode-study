"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # level order traversal
        # Each level put children nodes into queue
        # While the process,popped node points to the next(right) Node
        # Separate each level by putting None

        if not root:
            return root

        queue = deque([root, None])
        while queue:
            this_node = queue.popleft()
            if this_node:
                this_node.next = queue[0]
                if this_node.left:
                    queue.append(this_node.left)
                if this_node.right:
                    queue.append(this_node.right)
            else:
                if len(queue) != 0:
                    queue.append(None)

        return root
