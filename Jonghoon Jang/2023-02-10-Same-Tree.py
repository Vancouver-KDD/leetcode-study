"""
100. Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical,
and the nodes have the same value.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # Time complexity: O(n): single pass at most once
    # Space complexity: O(n): hash table used
    def isSameTree(self, p, q) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


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
