## Approach
- keep two pointers, slow and fast. While the slow moves one, the fast moves 2 - so if they meet true otherwise false
  
### Complexity
- Time complexity - O(n)
- Space complexity - O(n)

### Solution
```
# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} head
# @return {Boolean}
def hasCycle(head)
    slow, fast = head, head

    while fast && fast.next
        slow = slow.next
        fast = fast.next.next
        return true if slow == fast
    end

    false
end
```
