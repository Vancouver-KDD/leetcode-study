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
 //2023.02.05
 //Time Complexity: O(N)
 //Space Complexity: O(1)
class Solution {
    public ListNode reverseList(ListNode head) {
        if(head == null){
            return null;
        }

        ListNode preNode = null;
        while(head != null){

            ListNode nextNode = head.next;            
            head.next = preNode; 
            preNode = head;
            head = nextNode;
        }

        return preNode;
    }
}