/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int pairSum(ListNode head) {
        int answer = 0;
        

        ListNode slow = head;
        ListNode fast = head;

        while(fast != null && fast.next!= null){
            slow = slow.next;
            fast = fast.next.next;
        }

        slow = reversed(slow);
        fast = head;

        while(slow != null){
            if(answer < fast.val + slow.val){
                answer = fast.val + slow.val;
            }
            fast = fast.next;
            slow = slow.next;
        }


        return answer;
        
    }

    public ListNode reversed(ListNode head){
        ListNode prev = null;
        while(head != null){
            ListNode next = head.next;
            head.next = prev;
            prev = head;
            head = next;
        }
        return prev;
    }

}