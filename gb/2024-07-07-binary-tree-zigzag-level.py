import re


class Solution:
    def zigzgOrder(self, root):

        if not root:
            return []

        toggle = True  # left to right

        res = []
        # bfs
        queue = collections.deque()
        queue.append(root)

        currQSize = len(queue)
        subList = []
        while queue:
            currNode = queue.popleft()
            currQSize -= 1
            subList.append(currNode.val)

            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)

            if currQSize == 0:
                currQSize = len(queue)
                if toggle:
                    res.append(subList)
                    toggle = False
                else:
                    res.append(subList[::-1])
                    toggle = True
                subList = []

        return res
