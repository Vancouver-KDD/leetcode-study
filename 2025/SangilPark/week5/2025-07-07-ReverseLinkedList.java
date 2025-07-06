package week5;
import java.util.*;

/*
 * Week 5: Linked List
 * https://leetcode.com/problems/reverse-linked-list/
 */
class Solution {
    public static ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;

        while (curr != null) {
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }

    public static void main(String[] args) {
        int[] input = {1,2,3,4,5};
        ListNode head = new ListNode(1);
        reverseList(head);
    }

    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
}