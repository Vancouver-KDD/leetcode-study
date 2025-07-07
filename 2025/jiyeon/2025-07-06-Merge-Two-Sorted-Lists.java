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
class MergeTwoSortedLists {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode head = new ListNode();
        ListNode answer = head;

        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                answer.next = list1;
                list1 = list1.next;
            } else {
                answer.next = list2;
                list2 = list2.next;
            }
            answer = answer.next;
        }

        answer.next = list1 != null ? list1 : list2;

        return head.next;
    }
}