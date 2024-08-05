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
        #indexing of nodes starts at 1
        #The value is the same as the index #
        if not node:
            return None
        
        oldToNew = {}
        
        def dfs(node):
            if node in oldToNew:
                return
            
            newNode = Node(node.val)
            oldToNew[node] = newNode
            
            for neighbor in node.neighbors:
                dfs(neighbor)
                targetNode = oldToNew[neighbor]
                newNode.neighbors.append(targetNode)
            
            return
        
        
        dfs(node)
        return oldToNew[node]