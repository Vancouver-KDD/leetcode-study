class Solution:
    def search(self, nums: List[int], target: int) -> int:        
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if target >= nums[l] and target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if target >= nums[m] and target <= nums[r]:
                    l = m + 1                                 
                else:
                    r = m - 1
        return -1

class TimeMap:

    def __init__(self):
        # key : list of [val, timestamp]
        self.keyStore = {}  

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.keyStore.get(key, [])
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, tmp, cur = None, None, head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        dummy_node = cur = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = ListNode(list1.val)
                list1 = list1.next
            else:
                cur.next = ListNode(list2.val)
                list2 = list2.next
            cur = cur.next
        if list1 and not list2:
            cur.next = list1
        if list2 and not list1:
            cur.next = list2
        return dummy_node.next
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None:
            return
        left, right = head, head.next
        while right and right.next:
            left = left.next
            right = right.next.next
        second = left.next
        left.next = None
        prev = None
        
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp 
        
        while prev:
            tmp1 = head.next
            tmp2 = prev.next
            head.next = prev
            head.next.next = tmp1
            head = tmp1
            prev = tmp2
            

class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
    
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        oldToCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]
    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur = l1
        l1_str, l2_str = "", ""
        while cur:
            l1_str = str(cur.val) + l1_str
            cur = cur.next

        cur = l2
        while cur:
            l2_str = str(cur.val) + l2_str
            cur = cur.next
        res_str = str(int(l1_str) + int(l2_str))
        dummy_head = ListNode()
        dummy_head.next = ListNode()
        cur = dummy_head.next
        for i in range(len(res_str)-1,-1,-1):
            cur.val = int(res_str[i])
            if not i == 0:
                cur.next = ListNode()
                cur = cur.next
        return dummy_head.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
   
        if head == None or head.next == None:
            return False
        
        slow, fast = head, head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
            
        return False
    
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        return nums[fast]