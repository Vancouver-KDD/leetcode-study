import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        
        heap = []
        
        for i, node in enumerate(lists):
            heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode()
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = node
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, i, node))
            
        return dummy.next


solution = Solution()
lists = [ListNode(1, ListNode(4, ListNode(5, None))),
         ListNode(1, ListNode(3, ListNode(4, None))),
         ListNode(2, ListNode(6, None))]
print(solution.mergeKLists(lists))
      
      
