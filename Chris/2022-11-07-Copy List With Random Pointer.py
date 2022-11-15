"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        
        oldToNew = {}
        
        
        def copyRandom(headNode):
            
            if headNode == None:
                return None
            
            if headNode in oldToNew:
                return oldToNew[headNode]
            
            
            node = Node(headNode.val)
            
            
            oldToNew[headNode] = node
            
            
            node.next = copyRandom(headNode.next)
            node.random = copyRandom(headNode.random)
            
            
            return node
        
        
        return copyRandom(head)
        