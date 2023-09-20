# Using [::-1], o(n),o(n)
def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n_arr = []    

        while head:
            n_arr.append(head.val)
            head = head.next

        return n_arr == n_arr[::-1]   


# Two pointers,o(n),o(n)
def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        n_arr = []    

        while head:
            n_arr.append(head.val)
            head = head.next

        l,r = 0, len(n_arr)-1

        while l <= r:
            if n_arr[l] == n_arr[r]:
                l += 1
                r -= 1
            else:
                return False
        return True

# Two pointers (slow,fast), o(n), o(1)
def isPalindrome3(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        left,right = head,prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right =right.next
        
        return True