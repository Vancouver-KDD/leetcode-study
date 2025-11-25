from collections import deque

class Solution:
    def levelOrder(self, root):
        output = []
        if not root:
            return output

        level = 0
        queue = deque([root])
        while queue:
            output.append([])
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                output[level].append(node.val)

                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # go to next level
            level += 1

        return output