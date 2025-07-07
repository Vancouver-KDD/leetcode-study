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
class ReverseLinkedList {
    public ListNode reverseList(ListNode head) {
        ListNode answer = null;

        while (head != null) {
            ListNode temp = head.next;
            head.next = answer;
            answer = head;
            head = temp;
        }
        
        return answer;
    }
}