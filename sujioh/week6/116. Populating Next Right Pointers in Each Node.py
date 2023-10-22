from collections import deque


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        q = deque([root])

        while q:
            size = len(q)
            for i in range(size):
                node = q[0]
                q.remove(q[0])

                # each level's rightmost's next = None
                if i < size - 1:
                    node.next = q[0]

                # BFS
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root


'''Summary
BFS structure: queue, while, for 

1. while: while q exists 
2. for loop: 
    - remove a node from each iteration 
    - the right most node's next = None
    - add each node's right and left to stack 
'''
