#Given the root of a binary tree,
# invert the tree, and return its root.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: [TreeNode]) -> [TreeNode]:

        if root == None:
            return root

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

if __name__ == '__main__':
    # Create the binary tree
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    # Create an instance of the Solution class
    solution = Solution()

    # Invert the tree
    inverted_root = solution.invertTree(root)


    # Print the values of the inverted tree
    def print_tree(node):
        if node is None:
            return
        print(node.val)
        print_tree(node.left)
        print_tree(node.right)


    print_tree(inverted_root)