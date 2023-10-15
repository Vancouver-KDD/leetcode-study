class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        ListNode next = null;

        while (curr != null) {
            next = curr.next; 
            curr.next = prev; // set the flow goes to riverse
            prev = curr; // right now prev is 1
            curr = next; // move curr to the next node
        }
        return prev;

    }
}