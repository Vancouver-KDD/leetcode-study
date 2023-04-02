"""
98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # Time complexity: O(N) -> Single pass
    # Space complexity: O(N) -> stack
    def isValidBST(self, root) -> bool:

        def helper(root, min, max):
            if not root:
                return True

            if (root.left and root.left.val >= root.val) or root.val >= max:
                return False

            elif (root.right and root.right.val <= root.val) or root.val <= min:
                return False

            return helper(root.left, min, root.val) and helper(root.right, root.val, max)

        return helper(root, float("-inf"), float("inf"))


def main():
    s = Solution()


if __name__ == "__main__":
    main()
