class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0);
        ListNode result = dummy;

        while (head != null) {
            if (head.next != null) {
                // create a new node with the next node's value
                ListNode ls = new ListNode(head.next.val, new ListNode(head.val));
                //System.out.println(ls);
                result.next = ls;
                result = ls.next;

                head = head.next.next;

            } else {
                ListNode ls = new ListNode(head.val);
                result.next = ls;
                result = ls;
                head = head.next;
            }

        }

        //System.out.println(dummy.next);
        return dummy.next;
        
    }
}