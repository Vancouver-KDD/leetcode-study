
public class ReverseLinkedList {
	  public class ListNode {
		     int val;
		     ListNode next;
		     ListNode() {}
		      ListNode(int val) { this.val = val; }
		      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
		  }
	public ListNode reverseList(ListNode head) {
	      
        ListNode prev = null;
        ListNode next = null;
        ListNode current = head;
        while(current != null)
        {
            next = current.next;
            current.next = prev;
            prev = current;
            current = next;
            
        }
        head = prev;
        return head;
    }




}
