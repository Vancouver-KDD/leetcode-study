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
   * @return {void}
   */
  reorderList(head) {
    // 역순인 list를 만든다.
    // 역순list를 만들면서 list의 크기를 구한다.
    // list와 역순list를 번갈아 가면서 새로운 list에 값을 넣는다.
    // 횟수는 list크기 까지 한다.

    if (!head || !head.next) return;
    // 1. 중간 지점 찾기 (slow와 fast 포인터 사용)
    let slow = head;
    let fast = head;
    while (fast && fast.next) {
      slow = slow.next;
      fast = fast.next.next;
    }

    // 2. 중간 이후 리스트를 뒤집기
    let prev = null;
    let current = slow;
    while (current) {
      let nextNode = current.next;
      current.next = prev;
      prev = current;
      current = nextNode;
    }

    // 3. 앞부분과 뒷부분을 번갈아가며 병합
    let first = head;
    let second = prev; // 뒤집어진 리스트의 시작 (이제 리스트의 끝부분부터 시작)
    while (second && second.next) {
      let temp1 = first.next;
      let temp2 = second.next;

      first.next = second;
      second.next = temp1;

      first = temp1;
      second = temp2;
    }
  }
}
