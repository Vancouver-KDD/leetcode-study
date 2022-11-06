class Solution {
    public void reorderList(ListNode head) {
        if(head == null || head.next == null || head.next.next == null) return;

        // find center
        ListNode slow = head;
        ListNode fast = head;
        while(fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode center = null;
        if(fast.next == null) {
            center = slow.next;
            slow.next = null;
        } else {
            center = slow.next.next;
            slow.next.next = null;
        }

        ListNode pre = null;
        while(center.next != null) {
            ListNode next = center.next;
            center.next = pre;
            pre = center;
            center = next;
        }
        center.next = pre;

        ListNode front = head;
        ListNode rear = center;

        ListNode fNext;
        ListNode rNext;
        while(rear != null) {
            fNext = front.next;
            rNext = rear.next;

            front.next = rear;
            rear.next = fNext;

            front = fNext;
            rear = rNext;
        }
    }
}