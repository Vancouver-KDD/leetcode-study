"""
19. Remove Nth Node From End of List


Given the head of a linked list, remove the nth node from the end of the list and return its head.

#Ex.
Input: head = [1,2,3,(4),5], n = 2
Output: [1,2,3,5]

Input: head = [1,2], n = 1
Output: [1]

Input: head = [1,2], n = 1
Output: [1]

1 <= sz <= 30
1 <= n <= sz
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # Time complexity: O(n): single pass at most once
    # Space complexity: O(1): no extra space used
    def removeNthFromEnd(self, head, n):
        curr = head
        delayed = curr
        delayed_head = delayed
        # size 1
        if not curr.next:
            return None

        for _ in range(n):
            curr = curr.next
        # [1,2,3,(4),5]
        #      C
        # [1,2,3,(4),5]
        #  D

        # curr is None, just remove first node
        # [1, 2] N          n: 2   =>   [2]
        #  ()    C
        if not curr:  # curr: None
            return head.next

        # move D pointer to n-1 th node
        while curr.next:
            curr = curr.next
            delayed = delayed.next

        # [1,2,3,(4),5] N
        #            C
        # [1,2,3,(4),5] N
        #      D

        # remove nth node
        temp_next = delayed.next.next
        delayed.next = temp_next

        return delayed_head

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
    ll1 = s.create_linked_list([1,2,3,4,5])
    ll2 = s.create_linked_list([1,2])
    s.print_linked_list(s.removeNthFromEnd(ll1, 2))
    s.print_linked_list(s.removeNthFromEnd(ll2, 1))


if __name__ == "__main__":
    main()
