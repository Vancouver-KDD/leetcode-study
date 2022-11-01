// Similar Question
//  92. Reverse Linked List II
//  234. Palindrome Linked List 

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
//2022-10-26
//Time Complexity : O(n), Space Complexity: O(1)
class Solution{
    public ListNode reverseList(ListNode head){
        
        if(head == null){
            return null;
        }
        
        ListNode pre = null;
        ListNode next = null;

        while(head != null){
            next = head.next;
            head.next = pre;

            pre = head;
            head = next;
        }
        
        return pre;
    }
}
