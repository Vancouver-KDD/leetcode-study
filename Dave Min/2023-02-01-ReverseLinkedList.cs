/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode ReverseList(ListNode head) {
        ListNode prev = null;
        //ListNode curr = head;
        
        while(head != null){
            ListNode nextNode = head.next;            
            head.next = prev;    
            
            prev = head;            
            head = nextNode;            
        }
        
        return prev;
    }
}