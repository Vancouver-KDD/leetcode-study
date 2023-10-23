"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root

        if root.left:
            root.left.next = root.right

        if root.right and root.next:
            root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root