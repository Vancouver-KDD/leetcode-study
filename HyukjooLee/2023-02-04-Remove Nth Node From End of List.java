// Given the head of a linked list, remove the nth node from the end of the list and return its head

// Input: head = [1,2,3,4,5], n = 2
// Output: [1,2,3,5]

// using two pointers; fast and slow
// the fast pointer is moving one step more than slow pointer
// then, both pointers are traversed until fast pointer reaches the end of the list
// the next pointer of the node pointed to by slow pointer.. so that we can skip the linked node to be removed
// time complexity is O(N) which is the length of linked list
public ListNode removeNthFromEnd(ListNode head, int n) {
    // create a dummy node
    ListNode dummy = new ListNode(0);
    // set the dummy node's next to the head of the linked list
    dummy.next = head;
    
    // initialize two pointers, fast and slow, to the dummy node
    ListNode fast = dummy;
    ListNode slow = dummy;
    
    // advance fast n + 1 steps ahead of slow
    for (int i = 1; i <= n + 1; i++) {
        fast = fast.next;
    }
    
    // move both forward until fast reaches the end of the linked list
    while (fast != null) {
        fast = fast.next;
        slow = slow.next;
    }
    
    // update slow pointer to skip the node to be removed
    slow.next = slow.next.next;
    
    // return the dummy node's next node as the new head of the linked list
    return dummy.next;
}