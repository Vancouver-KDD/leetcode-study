"""
104. Maximum Depth of Binary Tree


Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path
 from the root node down to the farthest leaf node.
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # Time complexity: O(n): single pass at most once
    # Space complexity: O(n): n stacks
    def maxDepth(self, root):
        if not root:
            return 0
        left_longest = self.maxDepth(root.left)
        right_longest = self.maxDepth(root.right)
        return max(left_longest, right_longest) + 1

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
