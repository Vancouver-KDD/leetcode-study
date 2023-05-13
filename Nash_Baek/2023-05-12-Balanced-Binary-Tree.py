# For more description, please visit the blog below.


import random
class TreeNode:
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

class BinaryTree:
    def __init__(self):
        self.root_node = None
        self.left_length = 0
        self.right_length = 0

    
    def insert_value(self, value):
        if self.root_node is None:
            self.root_node = TreeNode(value)
        else:
            self._insert_value_recursive(self.root_node, value)

    def _insert_value_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left_child is None:
                current_node.left_child = TreeNode(value)
            else:
                self._insert_value_recursive(current_node.left_child, value)
        else:
            if current_node.right_child is None:
                current_node.right_child = TreeNode(value)
            else:
                self._insert_value_recursive(current_node.right_child, value)

    def convert_tree_to_list(self) -> list:
        result = []
        if self.root_node is None:
            return result

        queue = []
        queue.append(self.root_node)

        while queue:
            current_node = queue.pop(0)
            result.append(current_node.value)
            if current_node.left_child:
                queue.append(current_node.left_child)
            if current_node.right_child:
                queue.append(current_node.right_child)
        return result

    def print_node(self):
        print(self.convert_tree_to_list())


    def max_depth(self, node):
        if node is None:
            return 0
        else:
            self.left_length = self.max_depth(node.left_child)
            self.right_length = self.max_depth(node.right_child)

        if self.left_length > self.right_length:
            return self.left_length + 1
        else:
            return self.right_length + 1

    def longest_length(self):
        self.max_depth(self.root_node)
        print(self.right_length)

    def is_balanced_binary_tree(self):
        self.longest_length()
        return self.left_length == self.right_length

binary_tree = BinaryTree()

for _ in range(15):
    binary_tree.insert_value(random.randint(1, 100))

binary_tree.print_node()
print(binary_tree.is_balanced_binary_tree())