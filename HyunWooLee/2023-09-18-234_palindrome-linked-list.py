# Definition for singly-linked list.
class ListNode:
 def __init__(self, val=0, next=None):
     self.val = val
     self.next = next

class Solution:
    '''
    1. constraint is [1, 10^5] nodes
    2. reverse the second half to figure out palindrome.
    eg) [1,2,3,2*,1*] --> [1, 2] 3 [1*, 2*]
    - we can simply compare the array.

    - need to consider even and odd length.

    eg)

     s
    [1 2 3 2 1]
     f
         f
    [1 2 3 2 1]
       s
             f
    [1 2 3 2 1]
         s

    then reverse second half

    1->2->3     None <-2 <-1

    - then whether odd, or even length LL, we just have to go throuogh
    2 items each

    Runtime: O(n)
    space: O(1)
    '''

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse_linked_list(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev

        slow, fast = head, head

        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        reversed_start = reverse_linked_list(slow.next)
        slow.next = None

        while reversed_start:
            if reversed_start.val != head.val:
                return False
            reversed_start = reversed_start.next
            head = head.next
        # if required, then have a step to fix the modified linked list.
        return True
