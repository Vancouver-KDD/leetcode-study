package org.example;


public class RemoveElements {
  public ListNode removeElements(ListNode head, int val) {

    if (head == null) {
      return null;
    }

    // created dummy becasue if the first node is equal to val then it will be null
    ListNode dummy = new ListNode ();
    dummy.next = head;
    ListNode prev = dummy;
    ListNode curr = head;

    while (curr != null) {
      if (curr.val == val) {
        prev.next = curr.next;
      }else{
        prev = curr;
      }
      curr = curr.next;
    }
    return dummy.next;
  }

}