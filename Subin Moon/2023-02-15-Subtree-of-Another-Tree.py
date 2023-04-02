"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true

Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false

Constraints:
The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-104 <= root.val <= 104
-104 <= subRoot.val <= 104
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        # if not root or not subRoot:
        #     return False
        # if not root and not subRoot:
        #     return True
        #
        # def isSameTree(p, q):
        #     if p and q:
        #         return p.val == q.val and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        #     return p is q
        #
        # node = root
        # while node:
        #     if isSameTree(node, subRoot):
        #         return True
        #     else:
        #         return isSameTree(node.left, subRoot) or isSameTree(node.right, subRoot)
        def isSame(s, t):
            if not s and not t: return True
            if not s or not t: return False
            if s.val != t.val: return False
            return isSame(s.left, t.left) and isSame(s.right, t.right)

        if not root: return False
        if isSame(root, subRoot): return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSubtree_string(self, root, subRoot):
        def convert(tree):
            return "^" + str(tree.val) + "#" + convert(tree.left) + convert(tree.right) if tree else "$"

        return convert(subRoot) in convert(root)