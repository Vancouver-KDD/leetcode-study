# For more description, please visit the blog below.
# https://peterdrinker.tistory.com/485

class TreeNode:
    def __init__(self, parent=0, left_child=None, right_child=None):
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_value(self, value):
        """
        Inserting value into the node.

        :param value: the value to be inserted
        """
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive_helper(self.root, value)

    def _insert_recursive_helper(self, current_node, value):
        if value < current_node.parent:
            if current_node.left_child is None:
                current_node.left_child = TreeNode(value)
            else:
                self._insert_recursive_helper(current_node.left_child, value)
        else:
            if current_node.right_child is None:
                current_node.right_child = TreeNode(value)
            else:
                self._insert_recursive_helper(current_node.right_child, value)


    def search(self, value):
        return self._search_recursive_helper(self.root, value)
    
    def _search_recursive_helper(self, current_node, value):
        if current_node is None or current_node.parent == value:
            return value
        if value < current_node.parent:
            return self._search_recursive_helper(current_node.left_child, value)
        else:
            return self._search_recursive_helper(current_node.right_child, value)
        
    def inorder_traversal(self):
        self._inorder_traversal_recursive_helper(self.root)

    def _inorder_traversal_recursive_helper(self, current_node):
        if current_node is not None:
            self._inorder_traversal_recursive_helper(current_node.left_child)
            print(current_node.parent)
            self._inorder_traversal_recursive_helper(current_node.right_child)

    def binary_tree_to_list(self, root_node):
        """
        This method converts binary tree to list

        :param root_node: the root node to be converted
        """
        result = []
        if root_node is None:
            return result
        
        queue = []
        queue.append(root_node)

        while queue:
            node = queue.pop(0)
            result.append(node.parent)

            if node.left_child:
                queue.append(node.left_child)
            if node.right_child:
                queue.append(node.right_child)
        return result
    
    def print_node(self):
        if self.root is None:
            print("This is empty tree.")
            return
        
        print(self.binary_tree_to_list(self.root))

    def invert_tree(self, root_node):
        if root_node is None:
            return None
        
        # swap the children
        temp_child = root_node.left_child
        root_node.left_child = root_node.right_child
        root_node.right_child = temp_child

        self.invert_tree(root_node.left_child)
        self.invert_tree(root_node.right_child)
        return root_node
    
    def print_invert_node(self):
        if self.root is None:
            print("This is empty tree.")
            return
        inverted_node_list = self.binary_tree_to_list(self.invert_tree(self.root))
        print(inverted_node_list)

binary_tree = BinaryTree()
list = [4, 2, 7, 1, 3, 6, 9]
for element in list:
    binary_tree.insert_value(element)

# binary_tree.inorder_traversal()
binary_tree.print_node()
binary_tree.print_invert_node()
