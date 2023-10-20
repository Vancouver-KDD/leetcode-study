def connect(root):
    if not root:
        return root

    # Start from the root and move level by level
    level_start = root

    while level_start:
        curr = level_start

        # Traverse the current level and set the next pointers
        while curr:
            if curr.left:
                curr.left.next = curr.right

            if curr.right and curr.next:
                curr.right.next = curr.next.left

            curr = curr.next

        # Move to the next level's leftmost node
        level_start = level_start.left

    return root