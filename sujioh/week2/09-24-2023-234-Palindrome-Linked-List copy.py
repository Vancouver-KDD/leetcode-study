class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        # Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        prev = None
        curr = slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Compare the reversed second half with the first half
        first_half = head
        second_half = prev
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True


'''
Summary 
1. Find the middle node using two pointers (slow and fast).
2. Reverse the first half of the linked list.
3. Compare the reversed first half with the second half.

My mistakes 
1. The code correctly uses the prev node's value 
    as the starting point for the second half comparison.
2. Reverse logic
    - curr, prev, temp
    - prev = None
    - prev = curr 
'''
