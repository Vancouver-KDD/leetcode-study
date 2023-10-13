/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
var reverseBetween = function (head, left, right) {

    if (head == null) {
        return null;
    }

    if (left == right) {
        return head;
    }


    let reverseBeginning;
    let reverseEnd;
    let reverseTail;
    let res;
    let count = 1;

    if (head.next == null) {
        return head;
    }

    if (head.next.next == null) {
        temp = new ListNode(head.val, null);
        head = head.next;
        res = new ListNode(head.val, temp);
        return res;
    }

    while (head != null) {
        let temp;
        if (count < left) {
            if (res == null) {
                res = new ListNode(head.val, null);
            } else {
                temp = res;
                res = new ListNode(head.val, res);
            }
        }

        if (count > right) {
            temp = new ListNode(head.val, null);
            reverseEnd.next = temp;
        }

        if (count == left) {
            reverseBeginning = new ListNode(head.val, null);
            reverseEnd = reverseBeginning;
        }

        if (count > left && count <= right) {
            temp = new ListNode(head.val, reverseBeginning);
            reverseBeginning = temp;
            if (!res) {
                res = temp;
            }else{
                res.next = temp;
            }
        }

        count++;
        head = head.next;
    }

    return res;

};