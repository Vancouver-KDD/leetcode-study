"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        originalToClone = {}

        def makeClone(node):
            if node in originalToClone:
                return originalToClone[node]

            clone = Node(node.val)
            originalToClone[node] = clone

            for n in node.neighbors:
                clone.neighbors.append(makeClone(n))

            return clone

        if node:
            return makeClone(node)
        else:
            return None
