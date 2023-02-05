"""
143. Reorder List

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # Time complexity: O(n): single pass at most once
    # Space complexity: O(1): no extra space used
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # split into two halves
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None
        reversed_second = None
        while second_half:
            temp = second_half.next
            second_half.next = reversed_second
            reversed_second = second_half
            second_half = temp

        # 1, 2
        # 3, 4
        while reversed_second:
            temp1_next = head.next
            temp2_next = reversed_second.next
            head.next = reversed_second
            reversed_second.next = temp1_next
            head, reversed_second = temp1_next, temp2_next



    def create_linked_list(self, items):
        curr = None
        head = None
        for item in items:
            new_node = ListNode(item)
            if not head: # curr is None
                head = new_node
                curr = new_node
            else:
                curr.next = new_node
                curr = curr.next
        return head


    def print_linked_list(self, head):
        curr = head
        while curr:
            print(curr.val, end=' ')
            curr = curr.next
        print()


def main():
    s = Solution()


if __name__ == "__main__":
    main()
