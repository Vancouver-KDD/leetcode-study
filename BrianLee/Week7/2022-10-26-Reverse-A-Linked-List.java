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
    public ListNode reverseList(ListNode head) {
        if(head == null) return null;
        ListNode leaf = reverseCall(head);
        leaf.next = null;
        return root;
    }

    ListNode root = null;
    public ListNode reverseCall(ListNode head) {
        if(head.next == null) {
            root = head;
            return head;
        }

        ListNode node = reverseCall(head.next);
        node.next = head;
        return head;
    }
}