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

    # Time complexity: O(N) -> Single pass
    # Space complexity: O(N) -> Use hashmap
    def levelOrder(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [[root.val]]

        levels = {} # hashmap
        level = 0

        def traverse(root, levels, level):
            # base case
            if not root:
                return

            # in the same level
            if level in levels:
                levels[level].append(root.val)
            # new level
            else:
                levels[level] = [root.val]

            # traverse the next level
            traverse(root.left, levels, level + 1)
            traverse(root.right, levels, level + 1)

        traverse(root, levels, level)

        return levels.values()


def main():
    s = Solution()


if __name__ == "__main__":
    main()
