# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''
    Use two pointer approach
    - you can detect whether LL has a cycle or not.

    let:
     a = distance between start to beginning of cycle

     b = distance from beginning of cycle to where 2 pointers meet

     c = size of cycle

     - when slow and faster point meets together, we know for sure that faster pointer
     has cycled AT LEAST ONE or more time.
     - we don't know how many times.

     example 1:  1000, c = 2.
     - Then we know that by slow pointer hits the beginning of cycle, fast point has
      cycled through the loop MANY times.

     so, we can define this as
     0)   (slow pointer dist) = (fast pointer dist)/2
      - if slow pointer moved 10 units, then fast pointer moved 20 units

     1)  a + b = [ (a + b) + (n * c) ] /  2        //n could be 2, 3...100 we don't know but we know they always end
     up at same spot. Think like modulo operation. 11 % 2 is same as 97 % 2
     - use math to show step 0
     - from example 1, we dont know how many times fast pointer cycled through the loop,
     so we represent this as (n * c), where n is unknown integer.

     2) 2a + 2b = a + b + n * c

     3) a + b = n * c

     4) a  = (n * c) - b

     Now, why do we even need this?

     Let's assume the fast pointer is at intersection (at b)
     if we move (n * c) units, then we are exactly at the same spot.
     but if we move (n*c)-b spot, then we will be at the start of intersection.

     if we start a new pointer from start of linked list, and travel a unit, this means
     fast pointer will have moved (n*c) - b unit.

     - But we know that if faster pointer moves (n-c) - b unit, then we know its the beginning of cycle.
     - when both intersect, then we know it's the start of cycle.

    time: O(n)
    space: O(1)
    '''
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        # detect where slow and fast intersects
        while fast:
            # no cycle
            if not fast.next or not fast.next.next:
                return None
            slow = slow.next
            fast = fast.next.next

            # this is where we intersect.
            # slow pointer has travelled a + b
            # faster pointer travelled [(a + b) + n*C ]/2
            if slow == fast:
                break

        # at this point, we know cycle exists
        start = head

        # when start moves a unit, fast pointer would have moved n*c - b units
        # but we establisehd that a  = (n*c) - b
        # and that moving (n*c) - b from the intersection will get to start of cycle
        while start != fast:
            start = start.next
            fast = fast.next

        return fast