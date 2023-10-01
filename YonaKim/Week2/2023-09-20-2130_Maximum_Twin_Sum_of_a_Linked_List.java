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
        ListNode slow = head;
        ListNode fast = head;

        //find half point (slow) of linked list
        while(fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }

        //reverse second half of linked list
        ListNode reverseHead = null;
        ListNode placeHolder = null;

        while(slow != null) {
            placeHolder = slow.next;
            slow.next = reverseHead;
            reverseHead = slow;
            slow = placeHolder;
        }

        int maxSum = 0;

        //compute twin sum, update maximum twin sum
        while(reverseHead != null) {
            maxSum = Math.max(maxSum, head.val + reverseHead.val);
            head = head.next;
            reverseHead = reverseHead.next;
        }

        return maxSum;   
    }
}