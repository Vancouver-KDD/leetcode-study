/**
 * Leetcode
 * problem: 1721
 * link: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
 * tag: Linked List, Two Pointers
 */

/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapNodes(ListNode head, int k) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode temp = head, left = head, right = head;
        int length = 1;

        while (temp.next != null) {
            temp = temp.next;
            length++;
        }

        int l = length - k;
        while (k-- > 1) {
            left = left.next;
        }
        while (l-- > 0) {
            right = right.next;
        }
        if (left == right) {
            return head;
        }

        int tempVal = left.val;
        left.val = right.val;
        right.val = tempVal;

        return head;
    }
}