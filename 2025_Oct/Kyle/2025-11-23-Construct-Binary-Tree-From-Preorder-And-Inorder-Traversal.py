class Solution(object):
    def buildTree(self, preorder, inorder):
        # build a hashmap to store value -> its index relations
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        preorder_index = [0]

        def array_to_tree(left, right):
            # if there are no elements to construct the tree
            if left > right:
                return None

            # select the preorder_index element as the root and increment it
            root_value = preorder[preorder_index[0]]
            root = TreeNode(root_value)

            preorder_index[0] += 1

            # build left and right subtree
            # excluding inorder_index_map[root_value] element because it's the root
            root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
            root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

            return root

        return array_to_tree(0, len(preorder) - 1)