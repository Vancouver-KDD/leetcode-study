public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        
        boolean check = true;
        while(fast!=null){
            fast = fast.next;
            if(check){
                check = false;
            }
            else{
                check = true;
                slow= slow.next;
            }
            if(fast==slow){
                return true;
            }
        }
        
        return false;
    }
}