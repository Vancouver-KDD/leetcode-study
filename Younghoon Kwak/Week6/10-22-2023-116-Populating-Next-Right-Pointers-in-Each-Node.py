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
        if root==None:
            return None
        q=deque([[root,0]])
        d={}
        ans = []
        index = 0
        prev_line = ""
        arr = []
        while q:
            node,line= q.popleft()
            arr.append([node, line])
            if node.left:
                q.append([node.left,line+1])
            if node.right:
                q.append([node.right,line+1])


        for i in range(len(arr)):
            if i > 1:
                if arr[i][1] < arr[i-1][1]:
                    q[l-1][0].next = None
            if i >= 2:
                if arr[i][1] == arr[i-1][1]:
                    arr[i-1][0].next = arr[i][0]


        return root