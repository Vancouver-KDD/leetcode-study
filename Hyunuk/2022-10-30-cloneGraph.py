"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node):
            if node in hm:
                return hm[node]
            clone = Node(node.val)
            hm[node] = clone
            if node.neighbors:
                clone.neighbors = [dfs(n) for n in node.neighbors]
            return clone
            
        hm = dict()
        
        return dfs(node) if node else None
