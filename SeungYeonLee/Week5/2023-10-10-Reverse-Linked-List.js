/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (head) {

    if (head == null) {
        return null;
    }

    if (head.next == null) {
        return head;
    }

    let res = new ListNode(head.val, null);
    head = head.next;

    while (head != null) {
        let temp = res;
        res = new ListNode(head.val, temp);
        head = head.next;
    }

    return res;
};