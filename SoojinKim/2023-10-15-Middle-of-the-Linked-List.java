

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
class Solution {
    public ListNode middleNode(ListNode head) {
        int num = checkSize(head)/2;
        for(int i=0; i<num; i++){
            head = head.next;
        }
        return head;
    }
    public int checkSize(ListNode head){
        int count=0;
        while(head!=null){
            count ++;
            head = head.next;
        }
        return count;
    }
}