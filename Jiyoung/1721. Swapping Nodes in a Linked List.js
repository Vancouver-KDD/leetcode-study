var swapNodes = function (head, k) {
    let slow = fast = head;
    let prev = k-1;

    while (prev--) {
        fast = fast.next;
    }

    let left = fast;
    while (fast.next) {
        slow = slow.next;
        fast = fast.next;
    }

//swap value
    let tmp = slow.val;
    slow.val = left.val;
    left.val = tmp;

    return head;
};
