// 21. Merge Two Sorted Lists
// You are given the heads of two sorted linked lists list1 and list2.
// Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
// Return the head of the merged linked list.

var MergedTwoLists = (list1, list2) => {
    let dummyhead = new ListNode(); 
    //result linked list
    let current = dummyhead;
    
    while(list1 != null && list2 != null) {
        if(list1.val <= list2.val) {
            current.next = list1;
            list1 = list1.next;
        }else if(list1.val > list2.val) {
            current.next = list2;
            list2 = list2.next;
        }

        current = current.next;
    }

    if(list1 != null) current.next = list1;
    else current.next = list2;

    return dummyhead.next;
}