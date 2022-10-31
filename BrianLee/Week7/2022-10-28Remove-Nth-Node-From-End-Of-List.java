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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode pre = null;
        ListNode cur = head;

        ListNode end = head;
        for(int i = 0; i < n-1; i++) {
            end = end.next;
        }

        while(end.next != null) {
            pre = cur;
            cur = cur.next;
            end = end.next;
        }

        if(pre == null) return cur.next;
        pre.next = cur.next;
        return head;
    }
}