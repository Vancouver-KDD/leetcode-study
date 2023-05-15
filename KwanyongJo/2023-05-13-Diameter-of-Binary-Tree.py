# Given the root of a binary tree, return the length of the diameter of the tree.
#
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
# This path may or may not pass through the root.
#
# The length of a path between two nodes is represented by the number of edges between them.


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: [TreeNode]) -> int:
        self.max_diameter = 0
        self.getDiameter(root)
        return self.max_diameter

    #[1,2,3,4,5]
    def getDiameter(self, root):
        if not root:
            return 0
        print('root', root)
        print('getDiameter')
        left_depth = self.getDiameter(root.left)
        # root.left true
        #left_depth = self.getDiameter(self.getDiameter(root.left.left))

        #self.getDiameter(root.left.left) return 1

        # self.getDiameter( left_depth = 0)

        print('left_depth', left_depth)
        right_depth = self.getDiameter(root.right)
        print('right_depth', right_depth)
        # get the diameter between two nodes
        diameter = left_depth + right_depth

        # get the maximum diameter
        self.max_diameter = max(self.max_diameter, diameter)
        return max(left_depth, right_depth) + 1

if __name__ == '__main__':
    # Create the binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)


    solution = Solution()

    def print_tree(node):
        if node is None:
            return
        print(node.val)
        print_tree(node.left)
        print_tree(node.right)

    # print_tree(root)

    print(solution.diameterOfBinaryTree(root))