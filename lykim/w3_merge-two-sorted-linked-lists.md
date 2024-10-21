## Approach
- Compare the value of the current head of each list, then set the smaller head's next value recursively with the given method.
- If either list head is nil, return the other one

### Complexity
- Time complexity - O(nlog(n))
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
# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def merge_two_lists(l1, l2)
    return l2 if l1.nil? 
    return l1 if l2.nil?
    if l1.val < l2.val
        l1.next = merge_two_lists(l1.next, l2) # Start with the smaller head, then append the next ones as next
        return l1
    else
        l2.next = merge_two_lists(l1, l2.next)
        return l2
    end
end
```
