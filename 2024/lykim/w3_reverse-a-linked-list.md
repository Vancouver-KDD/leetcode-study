## Approach
- Create a new empty ListNode reversed, and set the head and the next value to the current head of the given ListNode and existing reversed ListNode respectively.


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
# @return {ListNode}
def reverse_list(head)
    reversed = nil

    while !head.nil?
        reversed = ListNode.new(head.val, reversed)  # the existing reversed list becomes the next 
        head = head.next
    end

    reversed
end
```
