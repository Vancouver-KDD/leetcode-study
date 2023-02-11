"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6


Input: lists = []
Output: []

Input: lists = [[]]
Output: []

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Solution 1: Two pointers
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        if not lists: return None
        if len(lists) == 1: return lists[0]

        def helper(list1, list2):
            res = ListNode(0)
            res_head = res
            while list1 and list2:
                if list1.val < list2.val:
                    res_head.next = list1
                    list1 = list1.next
                else:
                    res_head.next = list2
                    list2 = list2.next
                res_head = res_head.next

            if list1:
                res_head.next = list1
            elif list2:
                res_head.next = list2

            return res.next

        output = lists[0]
        output_head = output
        for i in range(1, len(lists)):
            output_head = helper(output_head, lists[i])

        return output_head

    # Solution 2: Heap
    def mergeKLists_Heap(self, lists):
        from heapq import heappush, heappop

        h = []
        for i, l in enumerate(lists):
            if l: heappush(h, (l.val, i))   # [(1, 0), (1, 1), (2, 2)]

        output = output_head = ListNode(0)
        while h:
            val, i = heappop(h)
            output_head.next = val
            if lists[i].next:
                heappush(h, (lists[i].next.val, i))
                lists[i] = lists[i].next
            output_head = output_head.next

        return output.next