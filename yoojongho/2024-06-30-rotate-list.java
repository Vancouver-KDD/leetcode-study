/**
 * Leetcode
 * problem: 61
 * link: https://leetcode.com/problems/rotate-list/
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
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null || head.next == null || k == 0) {
            return head;
        }

        int length = 1;
        ListNode temp = head;

        while (temp.next != null) {
            temp = temp.next;
            length++;
        }
        temp.next = head;
        k = k % length;
        k = length - k;

        while (k-- > 0) {
            temp = temp.next;
        }
        // 123451234512345..., head.val = 1, temp.val = 3
        head = temp.next;
        // 451234512345123..., head.val = 4, temp.val = 3
        temp.next = null;
        // 45213
        return head;
    }
}