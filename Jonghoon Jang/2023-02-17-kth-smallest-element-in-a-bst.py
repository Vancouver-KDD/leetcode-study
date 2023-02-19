"""
230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed)
 of all the values of the nodes in the tree.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # Time complexity: O(N) -> Single pass
    # Space complexity: O(N) -> stack
    def kthSmallest(self, root, k: int) -> int:
        sorted_list = []

        # Sort the values in the Tree using Inorder traverse
        def inorder_traverse(root, sorted_list):
            if root is not None:
                inorder_traverse(root.left, sorted_list)
                sorted_list.append(root.val)
                inorder_traverse(root.right, sorted_list)

        inorder_traverse(root, sorted_list)
        return sorted_list[k - 1]


def main():
    s = Solution()


if __name__ == "__main__":
    main()
