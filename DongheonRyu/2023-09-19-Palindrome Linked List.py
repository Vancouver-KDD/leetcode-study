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