# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. check edge cases for empty lists
        # 2. create a dummy node and set the dummy to a new tail
        # 3. compare the value of the nodes from each list, and add the lesser node to the tail
        # 4. move the pointer up from the list it was add from and also the tail
        # 5. repeat steps 3 and 4 until a either list is depleted
        # 6. add the remaining nodes to the end of the dummy
        # 7. return dummy.next as dummy holds nothing

        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        else:
            dummy = ListNode()
            tail = dummy

            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1.val
                    list1 = list1.next
                else:
                    tail.next = list2.val
                    list2 = list2.next
                tail = tail.next
            if list1:
                tail.next = list1
            else:
                tail.next = list2

            return dummy.next
