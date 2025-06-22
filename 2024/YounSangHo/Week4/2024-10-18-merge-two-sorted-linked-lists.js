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
   * @param {ListNode} list1
   * @param {ListNode} list2
   * @return {ListNode}
   */
  mergeTwoLists(list1, list2) {
    // It looks like a part of merge sort
    // merge sorted list after dvided as minimal
    let point1 = list1;
    let point2 = list2;
    const result = new ListNode(0, null);
    let resultPoint = result;

    while (point1 !== null || point2 !== null) {
      // if point1 and point2 have value, then compare each other
      if (point1 !== null && point2 !== null) {
        if (point2.val >= point1.val) {
          resultPoint.next = point1;
          point1 = point1.next;
        } else {
          resultPoint.next = point2;
          point2 = point2.next;
        }
      } else {
        if (point1 !== null) {
          resultPoint.next = point1;
          point1 = point1.next;
        } else {
          resultPoint.next = point2;
          point2 = point2.next;
        }
      }

      resultPoint = resultPoint.next;
    }

    return result.next;
  }
}
