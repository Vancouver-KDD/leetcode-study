from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # How to solve linked-list problems
        # 1. Convert the linked list to a regular list
        # nodeList = []
        # while head:
        #     nodeList.append(head.val)
        #     head = head.next
        # print(nodeList)

        # 2. Perform the required List operations
        # ex) 206 Reverse Linked List: nodeList = nodeList[::-1]

        # 3. Convert back to a Linked List
        # newHead = temp = ListNode()
        # for i in nodeList:
        #   temp.next = ListNode(i)
        #   temp = temp.next
        # return newHead.next

        # initialize the previous node, current node to None, head(param)
        prev, curr = None, head
        # until the current node exists, loop through
        while curr:
            # make a temporary node, which indicates the node - head.next
            nxt = curr.next
            # points to the curr.next to prev (pr
            curr.next = prev
            # move to the next element, iterate
            prev = curr
            curr = nxt
        return prev


s = Solution()
s.reverseList()
