"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
#         li = [[]]
#         tree = [root]
#         depth = 0
#         length = 1
#         prev_length = length
#         while tree:
#             length -= 1
#             temp = tree.pop(0)
#             if not temp: break
#             li[depth].append(temp.val)
#             if temp:
#                 tree.append(temp.left)
#                 tree.append(temp.right)
#             if length == 0:
#                 length = prev_length * 2
#                 prev_length = length
#                 depth += 1
#                 li.append([])
                
#         li.pop(-1)
#         new_node = Node()
#         new_root = new_node
#         for i in range(len(li)):
#             for j in li[i]:
#                 new_node.next = Node(j)
#                 new_node = new_node.next
#             if i < len(li)-1:
#                 new_node.next = Node("#")
#                 new_node = new_node.next
#         return new_root.next

        # hacking method for targeting this problem
        length = 1
        prev_length = length
        tree = [root]
        
        while tree:
            length -= 1
            temp = tree.pop(0)
            if not temp: break
            tree.append(temp.left)
            tree.append(temp.right)
            
            if length == 0:
                length = prev_length * 2
                prev_length = length
            else:
                temp.next = tree[0]
                
        return root