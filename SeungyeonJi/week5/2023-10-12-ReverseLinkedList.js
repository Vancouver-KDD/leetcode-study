var reverseList = function(head, prev = null) {
    if(!head) return prev

    //let's make holding point;
    let next = head.next;
    head.next = prev;

    return reverseList(next, head)
};