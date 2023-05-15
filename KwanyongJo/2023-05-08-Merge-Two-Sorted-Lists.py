# You are given the heads of two sorted linked lists list1 and list2.
#
# Merge the two lists in a one sorted list.
# The list should be made by splicing together the nodes of the first two lists.
#
# Return the head of the merged linked list.

# class Solution:
#     def mergeTwoLists(self, list1, list2):

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = temp = ListNode(0)
        while l1 != None and l2 != None:
            print('l1.val', l1.val)
            print('l2.val', l2.val)

            if l1.val < l2.val:
                temp.next = l1
                l1 = l1.next
            else:
                temp.next = l2
                l2 = l2.next
            temp = temp.next
        temp.next = l1 or l2
        return dummy.next

if __name__ == "__main__":
    s = Solution()

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(4)
    node1.next = node2
    node2.next = node3

    node11 = ListNode(1)
    node22 = ListNode(3)
    node33 = ListNode(4)
    node11.next = node22
    node22.next = node33


    def print_linked_list(head):
        current_node = head
        while current_node:
            print(current_node.val, end=" ")
            current_node = current_node.next
        print()




    print_linked_list(s.mergeTwoLists(node1, node11))