"""
572. Subtree of Another Tree

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure
 and node values of subRoot and false otherwise.

A subtree of a binary tree is a tree that consists of a node in tree and all of this node's descendants. The
 tree could also be considered as a subtree of itself.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # Time complexity: O(M * N): for every node N, check subRoot, M
    #  N: Number of nodes
    #  M: number of nodes in subRoot
    # Space complexity: O(M + N)
    def isSubtree(self, root, subRoot) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return self.isIdentical(root, subRoot)

        return self.isIdentical(root.left, subRoot) or self.isIdentical(root.right, subRoot)

    def isIdentical(self, s, t):
        # both s and t are None (None leaf)
        if not s and not t:
            return True
        # identical if val of s, t equal and left, right side of s, t are equal
        if s and t:
            return s.val == t.val and self.isIdentical(s.left, t.left) and self.isIdentical(s.right, t.right)
        return False


def main():
    s = Solution()


if __name__ == "__main__":
    main()
