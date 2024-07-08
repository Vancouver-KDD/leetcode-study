class Solution:
    def connect(self, root):
        if not root:
            return root

        queue = deque()
        queue.append(root)

        subList = []
        currQSize = len(queue)

        while queue:
            currNode = queue.popleft()
            subList.append(currNode)
            currQSize -= 1

            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)

            if currQSize == 0:
                subList.append(None)
                for i in range(len(subList)-1):
                    subList[i].next = subList[i+1]
                subList = []
                currQSize = len(queue)
        return root
