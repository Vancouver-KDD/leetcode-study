/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
  /**
   * @param {ListNode} head
   * @return {ListNode}
   */
  reverseList(head) {
    // reverse the linked list
    // I got node from the linkedList as squncely and put the node to stack for taking out to use FILO
    let point = head;
    let reverLi = null;

    // 포인트가 널이 되지 않는 시점 까지 반복
    while (point !== null) {
      // 새로운 노드를 포인터의 val와 변수 reverLi 사용 하여 만든다.
      let curNode = new ListNode(point.val, reverLi);
      // reverLi변수를 새롭게 만든 노드로 바꾼다.
      reverLi = curNode;
      // 변수 point를 point 다음 노드로 바꾼다.
      point = point.next;
    }

    return reverLi;
  }
}
