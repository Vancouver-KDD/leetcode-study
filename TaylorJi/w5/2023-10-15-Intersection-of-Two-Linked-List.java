public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if(headA == null || headB == null) {
            return null;
        }
        ListNode aP = headA;
        ListNode bP = headB;
        
        while (aP != bP) {
            if(aP == null) {
                aP = headB;
            } else {
                aP = aP.next;
            }
            
            if(bP == null) {
                bP = headA;
            } else {
                bP = bP.next;
            }
        
            }
            return aP;
            
        }
    } 