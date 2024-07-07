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
    public ListNode SwapNodes(ListNode head, int k) {
        ListNode firstNode = head;
        ListNode secondNode = head;

        while(k-1>0){
            firstNode = firstNode.next;
            k--;   
        }

        // while keeping k-gap, move two node parallelly till the first node ends.        
        ListNode kStepAhead = firstNode;
        while(kStepAhead.next!= null){
            kStepAhead = kStepAhead.next;
            secondNode = secondNode.next;
        }
        // swap two nodes.
        int temp = firstNode.val;
        firstNode.val = secondNode.val;
        secondNode.val = temp;

        return head;
    }
}
