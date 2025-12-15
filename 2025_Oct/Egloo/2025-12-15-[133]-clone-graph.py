"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        visited = dict()

        def clone(node):
            cloneNode = Node(val = node.val)
            visited[node.val] = cloneNode

            for n in node.neighbors:
                if not n.val in visited:
                    cloneNode.neighbors.append(clone(n))
                else:
                    cloneNode.neighbors.append(visited[n.val])
    
            return cloneNode

        if not node:
            return None

        return clone(node)