# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []
        level_counter = 0

        if not root:
            return []

        q.append(root)
        
        while q:
            curr_level = []
            level_counter += 1
            for _ in range(len(q)):
                curr_node = q.popleft()
                curr_level.append(curr_node.val)
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            if level_counter % 2 == 0:
                res.append(curr_level[::-1])
            else: 
                res.append(curr_level)
        return res