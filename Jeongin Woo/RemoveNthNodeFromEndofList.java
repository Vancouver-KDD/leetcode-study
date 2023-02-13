

public class RemoveNthNodeFromEndofList {
	  public class ListNode {
		     int val;
		     ListNode next;
		     ListNode() {}
		      ListNode(int val) { this.val = val; }
		      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
		  }
	  
	  public ListNode removeNthFromEnd(ListNode head, int n) {
	        
	        ListNode temp = new ListNode(0);
	        ListNode slow = temp;
	        ListNode fast = temp;
	         temp.next = head;
	        while(n >= 0){
	            fast = fast.next;
	            n--;
	        }
	        while(fast != null){
	            slow = slow.next;
	            fast = fast.next;
	        }
	        slow.next = slow.next.next;
	        return temp.next;
	}

}
