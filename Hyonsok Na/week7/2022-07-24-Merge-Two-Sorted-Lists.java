class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode curr = new ListNode(0);
        if(list1 == null) return list2;
        if(list2 == null) return list1;
        if(list1.val < list2.val) {
            curr = list1;
            list1 = list1.next;
        } else {
            curr = list2;
            list2 = list2.next;
        }
        curr.next = mergeTwoLists(list1, list2);
        return curr;
    }
}