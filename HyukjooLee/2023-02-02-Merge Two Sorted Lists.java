// You are given the heads of two sorted linked lists list1 and list2.
// Merge the two lists in a one sorted list. T
// he list should be made by splicing together the nodes of the first two lists.
// Return the head of the merged linked list.
	
// 1. using a node to keey track of the head of merged list 
// using two pointers list1 and list2 to traverse both lists
// tail is tracking of the last node in the merged list
// compare the values and add the smaller value between current nodes' value 
// between the two given lists
// time complexity is O(m + n): number of nodes in list1 and list2
// and a space complexity of O(1).
public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
	// will be the head of the merged list 
    ListNode merged = new ListNode();
	// to track the last node in the merged list
    ListNode tail = merged;
    while(list1 != null && list2 != null) {
		// compare the values
        if(list1.val < list2.val) {
			// add the smaller value
            tail.next = list1;
            list1 = list1.next;
        } else {
            tail.next = list2;
            list2 = list2.next;
        }
		// keep tracking the next node
        tail = tail.next;
    }
	//  to treat remaining nodes 
    tail.next = (list1 != null) ? list1 : list2;
    return merged.next;
}


// 2. using resursion 
// time complexity is O(m + n)
// space complexity is O(m + n) because of call stack
public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
    if (l1 == null) {
        return l2;
    }
    if (l2 == null) {
        return l1;
    }
    if (l1.val < l2.val) {
        l1.next = mergeTwoLists(l1.next, l2);
        return l1;
    } else {
        l2.next = mergeTwoLists(l1, l2.next);
        return l2;
    }
}