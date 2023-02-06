// You are given the head of a singly linked-list. The list can be represented as:
// L0 → L1 → … → Ln - 1 → Ln
// Reorder the list to be on the following form:
// You may not modify the values in the list's nodes. Only nodes themselves may be changed.

// L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
// [1          2          3           4] =>
// [1          4          2           3]
// first     last        second      second-last

input  [1,2,3,4,5,6,7,8]
output [1,8,2,7,3,6,4,5]
// seperate 2 parts based on the middle node of linked list 
[1->2->3->4->null]
[5->6->7->8->null]
// and reverse the second part
[8->7->6->5->null]
// divide => reverse => merge node by node

//
public void reorderList(ListNode head) {
     // in this case, we have nothing to do
     if(head == null || head.next == null) return;

     // head of first half   
     ListNode list1 = head;
     // head of second half
     ListNode slow = head;
     // tail of second half
     ListNode fast = head;
     // tail of first half
     ListNode prev = null;

     // this is how we divide the list into two part
     while(fast != null && fast.next != null) {
         prev = slow;
         slow = slow.next;
         fast = fast.next.next;
     }
     prev.next = null;

     ListNode list2 = reverse(slow);
     mergeTwoLists(list1, list2);
}

public ListNode reverse(ListNode head) {
    ListNode prev = null;
    ListNode current = head;
    while(current != null) {
        ListNode temp = current.next;
        current.next = prev;
        prev = current;
        current = temp;
    }
    
    head = prev;
    return head;
}

public void mergeTwoLists(ListNode list1, ListNode list2) {
    while(list1 != null) {
        ListNode list1_next = list1.next;
        ListNode list2_next = list2.next;
        list1.next = list2;
        if(list1_next == null) {
            break;
        }
        list2.next = list1_next;
        list1 = list1_next;
        list2 = list2_next;
    }
}