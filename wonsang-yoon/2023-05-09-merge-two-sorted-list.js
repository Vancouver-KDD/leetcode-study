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
var mergeTwoLists = function (list1, list2) {
    let mergedNode = new ListNode(null,null);
    let currentNode = mergedNode;
    while(list1 && list2){
        if(list1.val > list2.val){
            currentNode.next = list2
            list2 = list2.next
        }else{
            currentNode.next = list1
            list1 = list1.next
        }
        currentNode = currentNode.next;
    }
    currentNode.next = list1 || list2
    return mergedNode.next
};