var reverseList = function(head) {
    // base case
    if (head === null || head.next === null) {
        return head;
    }
    let reversedHead = reverseList(head.next);
    head.next.next = head;
    head.next = null;
    return reversedHead;
};