# For more description, please visit the blog below.

# Using depth search function, find the longest nodes
import random

class TreeNode:
    def __init__(self, value, left_child=None, right_child=None):
        self.left_child = left_child
        self.value = value
        self.right_child = right_child

class BinaryTree:
    def __init__(self):
        self.root_node = None

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
        result=[]
        if self.root_node is None:
            return result
        
        queue=[]
        queue.append(self.root_node)

        while queue:
            current_node = queue.pop(0)
            result.append(current_node.value)

            if current_node.left_child:
                queue.append(current_node.left_child)
            if current_node.right_child:
                queue.append(current_node.right_child)
        return result


    def print_as_list(self):
        print(self.convert_tree_to_list())

    def depth_first_search(self):
        return self._dfs_recursive_helper(self.root_node, [])

    def _dfs_recursive_helper(self, node, visited):
        if node is not None:
            visited.append(node.value)
            self._dfs_recursive_helper(node.left_child, visited)
            self._dfs_recursive_helper(node.right_child, visited)
        return visited
    
    def max_depth(self, node):
        if node is None:
            return 0
        else:
            left_depth = self.max_depth(node.left_child)
            right_depth = self.max_depth(node.right_child)
            
            # return the larger one
            if left_depth > right_depth:
                return left_depth + 1
            else:
                return right_depth + 1

    
    def print_max_depth(self):
        print(self.max_depth(self.root_node))


binary_tree = BinaryTree()

for _ in range(15):
    binary_tree.insert_value(random.randint(1,100))

binary_tree.print_as_list()
binary_tree.print_max_depth()