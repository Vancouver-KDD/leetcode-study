
public class Solution {
    public ListNode detectCycle(ListNode head) {
        // Initialize two pointers, slow and fast, to the head of the linked list.
    ListNode slow = head;
    ListNode fast = head;

    // move fast pointer by two and slow pointer by one
    while (fast != null && fast.next != null) {
      slow = slow.next;
      fast = fast.next.next;
      if (slow == fast) {
        // If the pointers meet, there is a cycle in the linked list.
        // Reset the slow pointer to the head of the linked list, and move both pointers one step at a time
        // until they meet again. The node where they meet is the starting point of the cycle.
        slow = head;
        while (slow != fast) {
          slow = slow.next;
          fast = fast.next;
        }
        return slow;
      }
    }
    return null;

    }
}

