# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_equal(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val == root2.val:
                return (is_equal(root1.left, root2.left) and is_equal(root1.right, root2.right))

            return False

        root_q = collections.deque([root])
        while root_q:
            root_node = root_q.pop()
            if is_equal(root_node, subRoot):
                return True
            if root_node.left:
                root_q.append(root_node.left)
            if root_node.right:
                root_q.append(root_node.right)
        return False                
            