from collections import deque


def largestValues(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        row_max = float('-inf') # Initialize the maximum value for the current row
        row_size = len(queue)

        for _ in range(row_size):
            node = queue.popleft()
            row_max = max(row_max, node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(row_max)

    return result
