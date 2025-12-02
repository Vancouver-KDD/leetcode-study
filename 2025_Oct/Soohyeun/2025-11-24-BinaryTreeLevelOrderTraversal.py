# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs -> using queue (FIFO) -> put all children nodes in the queue in each levels
        # -> count number of current level nodes -> iterate over n times : explore current level nodes
        if not root:
            return []

        queue = deque([root])
        res = []

        while queue:
            number_nodes = len(queue)
            level_nodes = []

            for _ in range(number_nodes):
                curr_node = queue.popleft()
                level_nodes.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            res.append(level_nodes)

        return res
