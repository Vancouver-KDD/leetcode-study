from typing import Optional


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Input: list1 = [], list2 = []
# Output: []

# Input: list1 = [], list2 = [0]
# Output: [0]

# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # TRY_3
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

        # TRY_2 - iterate one list and put nodes
        # # check if the two lists are none
        # if list1.next is None and list2.next is None:
        #     return None
        # elif list1.next is None:
        #     return list2
        # elif list2.next is None:
        #     return list1
        # else:
        #     prev_node = None
        #     curr_node = list1
        #     # next_node = None
        #     while list1.next:
        #         curr_val1 = list1.val
        #         while list2.next:
        #             curr_val2 = list2.val
        #             if curr_val1 <= curr_val2:
        #                 # if list1 value is less than or equal to list2 value,
        #                 # link prev_node -> curr_node -> next_node
        #                 prev_node = list2
        #                 prev_node.next = curr_node
        #                 prev_node = prev_node.next
        #                 curr_node.next = prev_node
        #             if curr_node.next:
        #                 curr_node = curr_node.next
        #         return list2
        #     return list2

            # TRY_1 - put two lists together and sort - O(n^3)
