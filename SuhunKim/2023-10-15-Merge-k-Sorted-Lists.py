# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # method 1 store it into list (n log n)
        merged_list = []
        for li in lists:
            node = li
            while node:
                merged_list.append(node.val)
                node = node.next
        merged_list.sort()
        
        new_node = ListNode()
        new_head = new_node
        
        for val in merged_list:
            new_node.next = ListNode(val)
            new_node = new_node.next
        
        return new_head.next

        # method 2 iterate over all list (O(k*len(lists[i]^2)))
        new_node = ListNode()
        new_head = new_node
        
        while lists:
            temp_min = pow(10,4)+1
            idx = -1
            to_pop = []
            for i in range(len(lists)):
                if not lists[i]:
                    to_pop.append(i)
                else:
                    if lists[i].val < temp_min:
                        temp_min = lists[i].val
                        idx = i
            if temp_min < pow(10,4)+1:
                new_node.next = ListNode(temp_min)
                new_node = new_node.next
            
            if lists[idx]:
                lists[idx] = lists[idx].next
            for j in range(len(to_pop)):
                lists.pop(to_pop[j])
                for k in range(j, len(to_pop)):
                    to_pop[k] -= 1
                    
        return new_head.next


        # method 3 iterate over all list (O(k*len(lists[i])))
        new_node = ListNode()
        new_head = new_node
        
        while lists:
            temp_min = pow(10,4)+1
            idx = -1
            i = 0
            
            while i < len(lists):
                if not lists[i]:
                    lists.pop(i)
                else:
                    if lists[i].val < temp_min:
                        temp_min = lists[i].val
                        idx = i
                    i += 1
            if temp_min < pow(10,4)+1:
                new_node.next = ListNode(temp_min)
                new_node = new_node.next
                lists[idx] = lists[idx].next
                    
        return new_head.next