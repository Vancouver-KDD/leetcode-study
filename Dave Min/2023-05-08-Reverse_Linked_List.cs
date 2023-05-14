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
            ListNode curr = head;
        while(curr!=null){
            ListNode nextTmp = curr.next; 

            curr.next = prev;
            prev = curr; 
            curr = nextTmp;
        }
        return prev;
    }
}

//TC : O(N)
//SC : O(1)
