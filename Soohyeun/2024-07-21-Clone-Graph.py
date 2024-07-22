"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val, [])

        while queue:
            this_node = queue.popleft()
            for neighbor in this_node.neighbours:
                if neighbor not in visited:
                    visted[neighbor] = Node(neigbor.val, [])
                    queue.append(neighbor)
            visited[this_node].neighbors.append(visted[neighbor]),

        return visited[node]