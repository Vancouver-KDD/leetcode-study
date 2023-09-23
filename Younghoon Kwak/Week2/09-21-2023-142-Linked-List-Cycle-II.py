class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        Edge case 1: There is no cycle
        Edge case 2: How to break the loop when there's cycle
        How do you find there's a cycle?

        """
        slow = head
        fast = head 

        i = 0
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            i = i + 1
            print("### Round %s ###" % i)
            print("Slow: %s " % slow.val)
            print("Fast: %s " % fast.val)
            if slow.val == fast.val:  
                print("### They met ###")
                print("After they met, Slow: %s " % slow.val)
                print("After they met, Fast: %s " % fast.val)
                slow = head
                print("### Resetting Slow: %s With the value %s ###" % (slow.val, head.val) )
                while slow != fast:
                    print("Util they meet, move just one for Slow : %s" % slow.val)
                    print("Util they meet, move just one for Fast: %s" % fast.val)
                    slow = slow.next
                    fast = fast.next
                print("They met again at: %s" % slow.val)
                return slow
            
        return None