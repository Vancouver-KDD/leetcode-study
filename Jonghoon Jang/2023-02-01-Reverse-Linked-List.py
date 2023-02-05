"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # Time complexity: O(n): single pass at most once
    # Space complexity: O(1):
    def reverseList(self, head):
        # while looping through the linked list
        # push curr node to new head(res)

        res = None
        curr = head

        while curr:
            temp_next = curr.next
            curr.next = res
            res = curr
            curr = temp_next
        return res

    # Time complexity: O(n): single pass at most once
    # Space complexity: O(n): extra space for stacks, it could go up to n levels deep
    def reverseListRecursive(self, head):

        res = None
        curr = head
        return self.help_reverse(curr, res)

    def help_reverse(self, head, res):
        if not head:
            return res
        # res: None
        # head: 1 2 3 4 5
        temp_next = head.next # 2-3-4-5
        head.next = res # 1-None
        res = head # res = 1-None
        head = temp_next # head = 2-3-4-5
        return self.help_reverse(head, res)

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
    ll2 = s.create_linked_list([1,2,3,4,5])
    s.print_linked_list(ll1)
    s.print_linked_list(s.reverseList(ll1))
    s.print_linked_list(s.reverseListRecursive(ll2))


if __name__ == "__main__":
    main()
