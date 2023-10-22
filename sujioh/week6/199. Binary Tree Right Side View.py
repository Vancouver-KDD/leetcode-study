import collections
#    1
#   / \
#  2   3
#   \   \
#    5   4
# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]


class Solution(object):
    def rightSideView(self, root):
        queue = collections.deque()
        res = []
        if root:
            queue.append(root)

        while queue:
            right_most_val = 0
            level_size = len(queue)
            for _ in range(level_size):
                curr = queue.popleft()
                right_most_val = curr.val  # the last assigned value
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(right_most_val)

        return res


'''
Breadth-First Search (BFS) 
- Utilizes a queue to explore nodes level by level.
- Tracks the rightmost value in each level.
    - right_most_val = curr.val  # the last assigned value
'''
