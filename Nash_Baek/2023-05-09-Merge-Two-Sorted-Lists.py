# For more description, please visit the blog below.
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head_node = None
    
    def insert_first_node(self, value):
        # new_node: [ value | next ]
        new_node = ListNode(value)
        if self.head_node is None:
            self.head_node = new_node
        else:
            new_node.next = self.head_node
            self.head_node = new_node

    def insert_last_node(self, value):
        new_node = ListNode(value)
        if self.head_node is None:
            self.head_node = new_node
        else:
            current_node = self.head_node
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def print_node(self):
        current_node = self.head_node
        while current_node:
            print(current_node.value, end=" ")
            current_node = current_node.next
        print()


class Solution:
    def mergeTwoLists(self, list1: LinkedList, list2: LinkedList) -> LinkedList:
        # Error handling part

        # Comparing the two linked list between each head nodes.
        # When there are two lists, A and B
        # If the value of current node A >= the value of current node B, the value of node B should be inserted into the linked list as the last node.
        # After that, the pointer of node B will move on to the next node.
        # If the value of current node A < the value of current node B, the value of node A should be inserted into the linked list as the last node.
        # After that, the pointer of node A will move on to the next node.
        # It requires O(N^2) time complexity due to the Brute Force algorithm.
        merged_two_lists = LinkedList()
        
        list1_current_node = list1.head_node
        list2_current_node = list2.head_node

        while list1_current_node is not None and list2_current_node is not None:
            if list1_current_node.value >= list2_current_node.value:
                merged_two_lists.insert_last_node(list2_current_node.value)
                list2_current_node = list2_current_node.next
            else:
                merged_two_lists.insert_last_node(list1_current_node.value)
                list1_current_node = list1_current_node.next

        while list1_current_node is not None:
            merged_two_lists.insert_last_node(list1_current_node.value)
            list1_current_node = list1_current_node.next

        while list2_current_node is not None:
            merged_two_lists.insert_last_node(list2_current_node.value)
            list2_current_node = list2_current_node.next
        
        # prints the merged linked list
        # merged_two_lists.print_node()
        return merged_two_lists
    
    
solution = Solution()
linked_list1 = LinkedList()
linked_list2 = LinkedList()
list1 = [1, 2, 4]
list2 = [1, 3, 4]

# convert the list into linked list by using insert method
for element in list1:
    linked_list1.insert_last_node(element)

for element in list2:
    linked_list2.insert_last_node(element)

linked_list1.print_node()
linked_list2.print_node()
print(solution.mergeTwoLists(linked_list1, linked_list2))
