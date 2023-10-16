/**
 * https://leetcode.com/problems/reverse-linked-list/
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
 Time Complexity: O(n) where n is the length of the linked list
 Space Complexity: O(1)
  */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode reverse = null;

        while(head != null) {
            ListNode dummy = reverse;
            reverse = new ListNode(head.val);
            reverse.next = dummy;
            head = head.next;
        }
        return reverse;
    }
}


/**
 * Recursion also possible.
 * Time Complexity: O(n) where n is the length of the Linked List
 * Space Complexity: O(n) due to implicit stack space due to recursion. Can be up to n levels deep.
 */
// class Solution {
    
//     public ListNode reverseList(ListNode head) {
//         if(head==null || head.next==null) return head;
        
//         ListNode p = reverseList(head.next);
//         head.next.next = head;
//         head.next=null;
        
//         return p;
//     }
// }