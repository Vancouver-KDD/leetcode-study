"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque 

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        
        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            
            new_node = Node(val=node.val)
            oldToNew[node] = new_node
            for n in node.neighbors:
                new_node.neighbors.append(dfs(n))
            return new_node
        return dfs(node) if node else None
        