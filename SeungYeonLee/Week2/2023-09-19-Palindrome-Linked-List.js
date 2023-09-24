/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function (head) {

    if (!head || !head.next) {
        return true;
    }

    let fast = head,
        slow = head;

    let reversed = [];

    while (fast && fast.next) {
        reversed.push(slow.val);
        slow = slow.next;
        fast = fast.next.next;
    }

    if(fast != null){
        slow = slow.next;
    }

    while (slow) {
        if (slow.val != reversed.pop()) {
            return false;
        }
        slow = slow.next;
    }

    reversed = [];

    return true;

};