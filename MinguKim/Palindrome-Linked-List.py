class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #Brute Force Method
        current = head
        array0 = []
        i=0
        while current:
            array0.append(current.val)
            current = current.next
        
        if len(array0) == 1:
            return True

        while array0[i] == array0[len(array0)-1-i]:
            if i == int(len(array0)/2):
                return True
            i+=1

        return False
