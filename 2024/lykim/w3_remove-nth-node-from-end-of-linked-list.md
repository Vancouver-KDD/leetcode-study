## Approach_1
- Use two pointers, the right one being `n` larger than the left pointer. once the right pointer reaches after the end of the linked list, the left pointer will be at nth element from the last.
- Then set the next node to be the following one.

### Complexity
- Time complexity - O(n)
- Space complexity - O(n)

### Solution
```
# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} head
# @param {Integer} n
# @return {ListNode}
def remove_nth_from_end(head, n)
    dummy = ListNode.new(0, head)
    left = dummy
    right = head

    while n > 0 && !right.nil? do
        right = right.next
        n -= 1
    end

    while !right.nil?
        left = left.next
        right = right.next
    end
    
    left.next = left.next.next

    dummy.next
end
```

https://leetcode.com/problems/remove-nth-node-from-end-of-list/
