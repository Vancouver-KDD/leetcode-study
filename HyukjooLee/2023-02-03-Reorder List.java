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


     // This code is dividing the linked list into two halves by using the fast and slow pointers. 
     // The fast pointer moves two steps at a time, 
     // while the slow pointer moves only one step. 
     // This way, when the fast pointer reaches the end of the list, the slow pointer is at the middle of the list.

    // The prev variable is used to keep track of the previous node of the slow pointer, 
    // which will be used to split the linked list into two halves. 
    // At the end of the loop, prev.next is set to null,
    // which means the end of the first half of the linked list.

    // Here's a detailed explanation of the loop:

    // Initialize the prev pointer to null, slow pointer to head, and fast pointer to head.
    // While fast is not null and fast.next is not null:
    // Set prev to slow.
    // Set slow to slow.next.
    // Set fast to fast.next.next.
    // Set prev.next to null, which cuts off the second half of the linked list and makes prev the last node of the first half.
     while(fast != null && fast.next != null) {
         prev = slow;
         slow = slow.next;
         fast = fast.next.next;
     }
     // disconnect ..
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