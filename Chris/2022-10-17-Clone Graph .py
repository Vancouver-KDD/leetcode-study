"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if node == None:
            return
        
        oldToNew = {}
        
        
        def dfs(old:'Node') ->'Node':
            
            if old in oldToNew:
                return oldToNew[old]
            
            new = Node(old.val)
            oldToNew[old] = new
            
            for v in old.neighbors:
                new.neighbors.append(dfs(v))
            
            return new
        
        return dfs(node)
            