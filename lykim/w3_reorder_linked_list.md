## Approach_1
- Reverse the last half of the linked list, then merge the first half and the second half.
- To find the half point, keep two pointers, slow and fast. While the slow moves one, the fast moves 2 - so the as the fast reaches to the end of the list, the slow will be at the mid point
  
### Complexity
- Time complexity - O(n)
- Space complexity - O(1)

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
# @return {Void} Do not return anything, modify head in-place instead.
def reorder_list(head)
    slow, fast = head, head.next

    while fast && fast.next
        slow = slow.next
        fast = fast.next.next
    end

    second = slow.next
    prev, slow.next = nil, nil
    
    # reversing the second half
    while second
        temp = second.next
        second.next = prev
        prev = second
        second = temp
    end

    # merge two halfs
    first, second = head, prev
    while second
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2
    end
end
```
