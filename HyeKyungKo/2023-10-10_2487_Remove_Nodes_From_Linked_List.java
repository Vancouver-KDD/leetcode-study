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
/*
Recursively call removeNodes to handle the tail first.
Then head.next node should have the biggest value.
Compare head.val and head.next.val,
if head.val < head.next.val,
should remove the current node,
return head.next,
otherwise we return head.
*/
//Time Complexity : O(N) <-- check every nodes 
//Space Complexity: O(N) <-- stack memory by recursive function 
class Solution {
    public ListNode removeNodes(ListNode head) {
        if(head == null){
            return null;
        }
        
        head.next = removeNodes(head.next);
        
        //if head.val < head.next.val, -> remove head 
        if(head.next != null && (head.val < head.next.val)){
            return head.next;
        }
        return head;
    }
}
