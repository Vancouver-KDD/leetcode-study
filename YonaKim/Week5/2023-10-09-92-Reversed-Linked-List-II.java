/**
 * https://leetcode.com/problems/reverse-linked-list-ii/
 */

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

/**
 * Time Complexity: O(N)
 * Space Complexity: O(N)
*/


class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if(head == null ||  head.next == null || left == right) {
            return head;
        }

        int index = 1;
        ListNode dummy = new ListNode();
        ListNode result = dummy;
        ListNode resultTail = null;
        //apend to result until we hit the left index
        while(head != null && index < left) {
            dummy.next = new ListNode(head.val);
            if(index == left-1) {
                resultTail = dummy.next;
            }
            dummy = dummy.next;
            head = head.next;
            index++;
        }

        //ListNode reverse = null;
        //reverse Linked List from left to right
         
        ListNode tail = null;
        dummy = null;
        while(index >= left && index <= right && head != null) {
            ListNode helper = new ListNode(head.val);
            if(index == left) {
                tail = helper;
            }
            helper.next = dummy;
            dummy = helper;
            head = head.next;
            index ++;
        }

        //append to result until we hit the end of the Linked List
        tail.next = head;
        if(resultTail != null) {
            resultTail.next = dummy;
        }

        return result.next;
        //return result;
    }
}

