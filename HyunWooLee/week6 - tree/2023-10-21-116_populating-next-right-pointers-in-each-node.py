
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        tmp = root
        queue = deque([root])
        while queue:
            prev = None
            for i in range(len(queue)):
                curr = queue.popleft()

                if i == 0:
                    prev = None
                else:
                    prev.next = curr
                prev = curr

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return tmp