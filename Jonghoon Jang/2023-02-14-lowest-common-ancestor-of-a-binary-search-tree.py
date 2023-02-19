"""
235. Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as
the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # Time complexity: O(N)
    # Space complexity: O(N)
    def lowestCommonAncestor(self, root, p, q):
        small = min(p.val, q.val)
        large = max(p.val, q.val)

        # base case
        if not root:
            return None

        # p or q is root
        if root.val == small or root.val == large:
            return root

        # p and q are left, right of root
        if small < root.val < large:
            return root

        # lca is in left subtree
        if small < root.val and large < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # lca is in riht subtree
        else:
            return self.lowestCommonAncestor(root.right, p, q)


def main():
    s = Solution()


if __name__ == "__main__":
    main()
