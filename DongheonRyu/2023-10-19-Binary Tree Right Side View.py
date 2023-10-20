def rightSideView(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_length = len(queue)
        for i in range(level_length):
            node = queue.popleft()

            # For each level, add the last (rightmost) node's value to the result
            if i == level_length - 1:
                result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result