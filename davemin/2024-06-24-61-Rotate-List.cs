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
    public ListNode RotateRight(ListNode head, int k) {
        if (head == null)
        {
            return null;
        }
        ListNode tail = head;
        int length = 1;
        while(tail.next != null){
            Console.WriteLine(tail.val);
            tail = tail.next;
            length++;
        }
        tail.next = head;
         k = length - k % length;
        while(k>0){
            head = head.next;
            tail = tail.next;            
            k--;
        }
        tail.next = null;
        return head;
    }
}
