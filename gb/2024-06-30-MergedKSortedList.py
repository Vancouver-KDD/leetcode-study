# Merge K sorted List

# You are given an array of "k" linked lists "lists", each linked list is sorted in accending order.
# Merge all the linked lists into one sorted linked list and return it

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]

# n = len(all element of lists), m = max(lists[i])
# O(n * logk)
# O(n)

class NodeList():
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        # merge 2 sorted linked list
        # O(N* logK)
        # []  []       []   []
        #  \  /         \   /
        #  [   ]         [   ]

        while len(lists) > 1:
            mergedLists = []
            # merge the pair of the list
            for i in range(0, len(lists), 2):
                left = lists[i]
                right = lists[i+1] if (i+1) < len(lists) else None

                mergedLists.append(self.merge(left, right))
            lists = mergedLists
        return lists[0]

    def merge(self, left, right):
        # SPACE complexity is O(N)
        dummyNode = NodeList()
        tail = dummyNode
        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        if right:
            tail.next = right
        if left:
            tail.next = left

        return dummyNode.next
