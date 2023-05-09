# For more description, please visit the blog below.

# class Solution:
#     def reverseList(self, head_node: Optional[ListNode]) -> Optional[ListNode]:

#         # Error check part
#         # 1. Checking the list size
#         # 2. Checking the boundary of values

#         # The value, next is the pointer which points the address of the next list.
#         # First of all, make the list of head_node to linked list.
#         # After that, change the value of next to the address of the previous list.

#         # for example, head_node is given as [1, 2, 3]

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head_node = None

    def delete_first_node(self):
        if self.head_node is None:
            raise ValueError("This node is empty.")
        else:
            self.head_node = self.head_node.next

    def delete_last_node(self):
        if self.head_node is None:
            raise ValueError("This node is empty.")
        else:
            current_node = self.head_node
            while current_node.next.next:
                current_node = current_node.next
            current_node.next = None

    def reverse_node(self):
        if self.head_node is None:
            raise ValueError("This node is empty.")
        else:
            previous_node = None
            current_node = self.head_node
            while current_node:
                temp_node = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = temp_node
            return previous_node
        
    def insert_first_node(self, data):
        new_node = ListNode(data)
        if self.head_node is None:
            self.head_node = new_node
        else:
            new_node.next = self.head_node
            self.head_node = new_node

    def insert_last_node(self, data):
        new_node = ListNode(data)
        if self.head_node is None:
            self.head_node = new_node
        else:
            current_node = self.head_node
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node


    def print_list(self):
        current_node = self.head_node
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

linked_list = LinkedList()
linked_list.insert_first_node(1)
linked_list.insert_last_node(2)
linked_list.insert_last_node(3)
linked_list.insert_last_node(4)
linked_list.insert_first_node(-1)
linked_list.insert_last_node(5)
linked_list.print_list()