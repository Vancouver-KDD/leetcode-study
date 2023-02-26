"""
230. Kth Smallest Element in a BST

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed)
 of all the values of the nodes in the tree.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTree(preorder, inorder):
        # Create a dictionary to store the index of each node value in the inorder traversal
        inorder_map = {}
        for i, val in enumerate(inorder):
            inorder_map[val] = i

        def buildSubtree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int) -> TreeNode:
            if preorder_left > preorder_right:
                return None

            # The root node is the first element of the preorder traversal
            root_val = preorder[preorder_left]
            root = TreeNode(root_val)

            # Find the index of the root node in the inorder traversal
            inorder_root_index = inorder_map[root_val]

            # Recursively construct the left and right subtrees
            root.left = buildSubtree(preorder_left + 1, preorder_left + inorder_root_index - inorder_left, inorder_left,
                                     inorder_root_index - 1)
            root.right = buildSubtree(preorder_left + inorder_root_index - inorder_left + 1, preorder_right,
                                      inorder_root_index + 1, inorder_right)

            return root

        # Call the recursive function with the full range of indices
        return buildSubtree(0, len(preorder) - 1, 0, len(inorder) - 1)


def main():
    s = Solution()


if __name__ == "__main__":
    main()
