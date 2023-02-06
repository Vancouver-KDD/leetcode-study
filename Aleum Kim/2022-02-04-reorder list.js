var reorderList = function(head) {
    const mid = getMid(head);           /* Time O(N) */
    const reveredFromMid = reverse(mid);/* Time O(N) */

    reorder(head, reveredFromMid);      /* Time O(N) */
};

const getMid = (head) => {
    let [ slow, fast ] = [ head, head ];

    while (fast && fast.next) {         /* Time O(N) */
        slow = slow.next;
        fast = fast.next.next;
    }

    return slow;
}

const reverse = (head) => {
    let [ prev, curr, next ] = [ null, head, null ];

    while (curr) {                      /* Time O(N) */
        next = curr.next;
        curr.next = prev;

        prev = curr;
        curr = next;
    }

    return prev;
}

const reorder = (l1, l2) => {
    let [ first, next, second ] = [ l1, null, l2 ];

    while (second.next) {              /* Time O(N) */
        next = first.next;
        first.next = second;
        first = next;

        next = second.next;
        second.next = first;
        second = next;
    }
}