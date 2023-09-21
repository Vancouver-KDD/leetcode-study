class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # ### method 1 (Using list) ###
        li = []
        curr = head
        while curr:
            li.append(curr.val)
            curr = curr.next
        return li[:(len(li)+1)//2] == list(reversed(li[len(li)//2:]))