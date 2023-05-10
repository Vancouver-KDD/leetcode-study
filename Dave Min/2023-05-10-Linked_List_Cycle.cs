/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if(head ==null || head.next == null) return false;
        ListNode hare = head.next;
        ListNode tortoise = head;
        while(hare!=null && hare.next!=null ){
            if(hare == tortoise) return true;
            hare = hare.next.next;
            tortoise = tortoise.next;
        }
        return false;
    }
}

//TC: O(N)
//SC: O(1)
