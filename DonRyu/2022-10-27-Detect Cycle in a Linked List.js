var removeNthFromEnd = function (head, n) {
    // Create a new LinkedList with a dummy first entry that copies the original LinkedList
    let newLinkedList = new ListNode(0);
    newLinkedList.next = head;

    // Initialise fast and slow pointers
    let fastPointer = newLinkedList;
    let slowPointer = newLinkedList;

    // Move the fast pointer up by n + 1 (+ 1 is to account for the dummy node)
    for (let i = 1; i <= n + 1; i++) {
        fastPointer = fastPointer.next;
    }

    // Move the fast and slow pointers fowards, until the fast pointer reaches the end
    // This indicates that the slow pointer has reached (end - n - 1) AKA the next node is the target node
    while (fastPointer != null) {
        fastPointer = fastPointer.next;
        slowPointer = slowPointer.next;
    }

    // Move the slow pointer's next value on by 1 (effectively skipping / removing the target node)
    slowPointer.next = slowPointer.next.next;

    // Return the copy of the original list node, minus the initial dummy node and the node that was removed
    return newLinkedList.next;
};
