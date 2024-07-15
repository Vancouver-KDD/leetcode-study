# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        
        q = collections.deque()
        q.append((root, ""))
        ans = []

        while q:
            c_node, path = q.popleft()
            if not c_node.left and not c_node.right:
                path += str(c_node.val)
                ans.append(path)
            if c_node.left:
                q.append((c_node.left, path + str(c_node.val) + "->"))
            if c_node.right:
                q.append((c_node.right, path + str(c_node.val) + "->"))
        return ans