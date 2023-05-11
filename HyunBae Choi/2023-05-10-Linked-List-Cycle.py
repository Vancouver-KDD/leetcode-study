# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Constraints:
# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 1. create 2 pointers and start them both at head (going to use Floyd-Warshall algorithm, or Floyd's algorithm for short)
# 2. loop through the linked lists while the pointer moving 2 increments
#    and the next value (since we are moving it by 2) is not null
# 3. check if the two pointers are at the same address each iteration and if they are, there is a loop
# 4. else, the linked list does not have a loop


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointer_one_increment = head
        pointer_two_increments = head

        while pointer_two_increments and pointer_two_increments.next:
            pointer_one_increment = pointer_one_increment.next
            pointer_two_increments = pointer_two_increments.next.next

            if pointer_one_increment == pointer_two_increments:
                return True

        return False
