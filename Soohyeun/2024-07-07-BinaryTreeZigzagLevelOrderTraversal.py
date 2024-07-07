# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Use 2 stacks: left_stack, right_stack
        # while loop until both stacks are empty
        # inner while loop, put children into the other stack until the stack gets empty
        # when node is put into the new stack, append into List
        if not root:
            return []
        res = [[root.val]]
        left_stack, right_stack = [], [root]

        while left_stack or right_stack:
            temp_res = []
            while left_stack:
                this_node = left_stack.pop()
                if this_node.left:
                    temp_res.append(this_node.left.val)
                    right_stack.append(this_node.left)
                if this_node.right:
                    temp_res.append(this_node.right.val)
                    right_stack.append(this_node.right)
            if temp_res:
                res.append(temp_res)
            temp_res = []
            while right_stack:
                this_node = right_stack.pop()
                if this_node.right:
                    temp_res.append(this_node.right.val)
                    left_stack.append(this_node.right)
                if this_node.left:
                    temp_res.append(this_node.left.val)
                    left_stack.append(this_node.left)
            if temp_res:
                res.append(temp_res)

        return res