# For more description, please visit the blog below.
# https://peterdrinker.tistory.com/488

import random

class TreeNode:
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child


class BinaryTree:
    def __init__(self):
        self.root_node = None
        self.max_length = 0

    def insert_value(self, value):
        if self.root_node is None:
            self.root_node = TreeNode(value)
        else:
            self._insert_value_recursive(self.root_node, value)

    def _insert_value_recursive(self, current_node, value):
        if value < self.root_node.value:
            if current_node.left_child is None:
                current_node.left_child = TreeNode(value)
            else:
                self._insert_value_recursive(current_node.left_child, value)
        else:
            if current_node.right_child is None:
                current_node.right_child = TreeNode(value)
            else:
                self._insert_value_recursive(current_node.right_child, value)
    
    def convert_tree_to_list(self):
        result = []
        queue = []
        if self.root_node is None:
            return result
        
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
            left_depth = self.max_depth(node.left_child)
            right_depth = self.max_depth(node.right_child)

            self.max_length = max(self.max_length, left_depth + right_depth)

            if left_depth > right_depth:
                return left_depth + 1
            else:
                return right_depth + 1
        
    def longest_path(self):
        self.max_depth(self.root_node)
        return self.max_length


binary_tree = BinaryTree()

for _ in range(15):
    binary_tree.insert_value(random.randint(1, 100))

binary_tree.print_node()
print(binary_tree.longest_path())