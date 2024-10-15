## Approach_1
- Use Hash structure to record the frequency of each element. Then use the largest k values to get the key
- There's an array method `tally` doing the same job too

### Complexity
- Time complexity - O(nlog(n)) due to sorting
- Space complexity - O(n) with the Hash creation & result array creation of O(k)

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
    
end
```

https://leetcode.com/problems/remove-nth-node-from-end-of-list/
