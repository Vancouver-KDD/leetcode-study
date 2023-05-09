# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:

        #head = [1,2,3,4,5]

        new_list = None
        curr = head

        while curr :
            next_node = curr.next

            curr.next = new_list
            new_list = curr
            curr = next_node

        return new_list





