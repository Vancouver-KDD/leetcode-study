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
   * @param {number} n
   * @return {ListNode}
   */
  removeNthFromEnd(head, n) {
    // 전체 노드 개수 확인
    // 노드 개수 에서 n을 뺀 값의 번째 를 제거

    let point = head;
    let length = 0;
    let removeId = 0;
    while (point !== null) {
      point = point.next;
      length++;
    }

    console.log(`length: ${length}`);
    if (length === 1) return head.next;

    removeId = length - n;
    point = head;
    if (removeId === 0) return head.next;
    for (let i = 1; i < removeId; i++) {
      point = point.next;
      console.log(point);
    }

    point.next = point.next.next;

    return head;
  }
}
