# https://leetcode.com/problems/subtree-of-another-tree/


class TreeNode:
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

class BinaryTree:
    def __init__(self):
        self.root_node = None
    
    def insert_node_bst(self, value):
        if self.root_node is None:
            self.root_node = TreeNode(value)
        else:
            self._insert_node_bst(self.root_node, value)

    def _insert_node_bst(self, current_node, value):
        if value < current_node.value:
            if current_node.left_child is None:
                current_node.left_child = TreeNode(value)
            else:
                self._insert_node_bst(current_node.left_child, value)
        else:
            if current_node.right_child is None:
                current_node.right_child = TreeNode(value)
            else:
                self._insert_node_bst(current_node.right_child, value)

    def insert_node(self, value):
        if self.root_node is None:
            self.root_node = TreeNode(value)
        else:
            self._insert_node(self.root_node, value)

    def _insert_node(self, current_node, value):
        if current_node.left_child is None:
            current_node.left_child = TreeNode(value)
        elif current_node.right_child is None:
            current_node.right_child = TreeNode(value)
        else:
            self._insert_node(current_node.left_child, value)


    def convert_tree_to_list(self):
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

class Solution:
    def is_sub_tree(self, root, subRoot) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        return self.is_same_tree(root, subRoot) or self.is_sub_tree(root.left_child, subRoot) or self.is_sub_tree(root.right_child, subRoot)
    
    def is_same_tree(self, node_a, node_b):
        if not node_a and not node_b:
            return True
        if not node_a or not node_b:
            return False
        return node_a.value == node_b.value and self.is_same_tree(node_a.left_child, node_b.left_child) and self.is_same_tree(node_a.right_child, node_b.right_child)

            
        
solution = Solution()

binary_tree1 = BinaryTree()
binary_tree1.insert_node(3)
binary_tree1.insert_node(4)
binary_tree1.insert_node(5)
binary_tree1.insert_node(1)
binary_tree1.insert_node(2)
binary_tree1.insert_node(None)
binary_tree1.insert_node(None)
binary_tree1.insert_node(None)
binary_tree1.insert_node(None)
binary_tree1.insert_node(0)

binary_tree2 = BinaryTree()
binary_tree2.insert_node(4)
binary_tree2.insert_node(1)
binary_tree2.insert_node(2)

print(solution.is_sub_tree(binary_tree1.root_node, binary_tree2.root_node))

print(binary_tree1.convert_tree_to_list())
print(binary_tree2.convert_tree_to_list())