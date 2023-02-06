/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    let mergedList = tail = new ListNode();

    while (list1 && list2) {
        const isL2Greater = list1.val <= list2.val;
        const isL2Less = list2.val < list1.val;

        if (isL2Greater) {
            tail.next = list1;
            list1 = list1.next;
        }
        if (isL2Less) {
            tail.next = list2;
            list2 = list2.next;
        }
        tail = tail.next;
    }

    tail.next = list1 || list2;

    return mergedList.next;
};