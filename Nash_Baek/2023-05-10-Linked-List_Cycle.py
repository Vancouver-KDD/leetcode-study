# For more description, please visit the blog below.
# https://peterdrinker.tistory.com/484

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head_node = None

    def insert_first_node(self, value):
        new_node = ListNode(value)
        if self.head_node is None:
            self.head_node = new_node
        else:
            # new_node [ value / next ] -> head_node [ value / next ]
            new_node.next = self.head_node
            self.head_node = new_node

    def insert_last_node(self,value):
        new_node = ListNode(value)
        if self.head_node is None:
            self.head_node = new_node
        else:
            # current_node [ value / next ] -> new_node
            current_node = self.head_node
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def delete_first_node(self):
        if self.head_node is None:
            raise ValueError("This list is empty.")
        elif self.head_node.next:
            # delete head_node [ value / next ] and move the head_node to next node
            self.head_node = self.head_node.next
        else:
            self.head_node = None

    def delete_last_node(self):
        if self.head_node is None:
            raise ValueError("This list is empty.")
        else:
            current_node = self.head_node
            while current_node.next.next:
                current_node = current_node.next
            current_node.next = None
    
    def count_number_node(self) -> int:
        if self.head_node is None:
            return 0
        else:
            current_node = self.head_node
            counter = 0
            while current_node:
                counter += 1
                current_node = current_node.next
            return counter

    def print_node(self):
        current_node = self.head_node
        while current_node:
            print(current_node.value, end= " ")
            current_node = current_node.next
        print()


class Solution:
    def hasCycle(self, linked_list: LinkedList) -> bool:
        pos = 3
        current_pos = 0
        current_node = linked_list.head_node

        # Check the boundary with pos and the size of linked list.
        if pos > linked_list.count_number_node() - 1:
            pos = -1
            return False

        # Find the pointer of the [pos]th node of linked list.
        while current_pos == pos:
            current_node = current_node.next
            current_pos += 1
        
        last_node = linked_list.head_node
        while last_node.next:
            last_node = last_node.next
        
        if last_node.next == None:
            last_node.next = current_node
        else:
            pos = -1
        return pos != -1

solution = Solution()
list = [3, 2, 0, 4]
linked_list = LinkedList()
for element in list:
    linked_list.insert_last_node(element)
linked_list.print_node()
print(solution.hasCycle(linked_list))