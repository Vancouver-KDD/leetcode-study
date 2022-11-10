"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # check node is not empty
        if not node:
            return
        return self.dfs_deep_copy(node, {})
        
        
    
    def dfs_deep_copy(self, node: 'Node', visit: Dict['Node', 'Node']) -> 'Node':
        copy_node = Node(node.val, [])
        
        # write current node is visited
        visit[node] = copy_node
        
        # traversal all neighbors
        for neighbor in node.neighbors:
            if neighbor in visit:
                copy_node.neighbors.append(visit[neighbor])
            else:
                copy_node.neighbors.append(self.dfs_deep_copy(neighbor, visit))
        
        return copy_node