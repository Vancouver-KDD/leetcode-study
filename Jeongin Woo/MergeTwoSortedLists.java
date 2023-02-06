

public class MergeTwoSortedLists {
	  public class ListNode {
		     int val;
		     ListNode next;
		     ListNode() {}
		      ListNode(int val) { this.val = val; }
		      ListNode(int val, ListNode next) { this.val = val; this.next = next; }
		  }
	  
	public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode empty = new ListNode(0);
        ListNode start = empty;
        if(list1 == null) return list2;
        if(list2 == null) return list1;

        while(list1 != null && list2 != null){
            
            if(list1.val < list2.val){
                start.next = list1;
                list1 = list1.next;

            }else{
                start.next = list2;
                list2 = list2.next;
            }

            start = start.next;
        }
        if(list1 == null)
            start.next = list2;
        if(list2 == null)
            start.next = list1;
   
        return empty.next;
    }


}
