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
            return None
        # adjList
        copyDict = {}
        queue = deque()
        queue.append(node)

        while queue:
            old = queue.popleft()
            if old not in copyDict:
                copyDict[old] = Node(old.val)
            new = copyDict[old]
            for nei in old.neighbors:
                if nei not in copyDict:
                    copyDict[nei] = Node(nei.val)
                    queue.append(nei)
                newNei = copyDict[nei]
                newNei.neighbors.append(new)
        return copyDict[node]

        # 1-[2, 4]: 1-[2, 4]
        # 2-[1, 3]: 2-[1, 3]
        # 3-[2, 4]: 3-[2, 4]
        # 4-[1, 3]: 4-[1, 3]
