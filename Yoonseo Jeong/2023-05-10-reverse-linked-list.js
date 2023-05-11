var reverseList = function(head) {
    // check if parameter is null or empty
    if(!head) {
        return null
    }
    // check if linked list only contains one node
    if(!head.next) {
        return head
    }
    // first item
    let first = head
    // next item of first item
    let second = first.next
    // loop until last item (that does not have next item)
    while(second) {
        // save third item
        const temp = second.next
        // second item's next is linked to first item (previous item)
        second.next = first
        // second item is now first
        first = second
        // third item is now second
        second = temp
        // previous first item is linked to current first's next
    }
    // original first item's next is now pointing to null
    head.next = null
    // original last item is now the head
    head = first
    return head

    // complexity
    // time: O(n)
    // space: O(1)
};