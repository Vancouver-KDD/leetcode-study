// Given the head of a linked list,
//todo: return the node where the cycle begins. If there is no cycle, return null.

// There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is null if there is no cycle. Note that pos is not passed as a parameter.

// Do not modify the linked list.

//* Example 1:

// Input: head = [3,2,0,-4], pos = 1
// Output: tail connects to node index 1
// Explanation: There is a cycle in the linked list, where tail connects to the second node.

//* Example 2:

// Input: head = [1,2], pos = 0
// Output: tail connects to node index 0
// Explanation: There is a cycle in the linked list, where tail connects to the first node.

//* Example 3:

// Input: head = [1], pos = null
// Output: no cycle
// Explanation: There is no cycle in the linked list.

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function (head) {
  // Edge case: an empty list or a list with a single node has no cycle
  if (!head || !head.next) {
    return null;
  }

  // slow and fast starts from the same point
  let slow = head;
  let fast = head;
  while (fast && fast.next && fast.next.next) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) {
      // if there is a cycle
      slow = head; // slow starts from the head
      while (slow !== fast) {
        // slow and fast meet at the start of the cycle
        slow = slow.next; // slow and fast move at the same speed
        fast = fast.next; // slow and fast meet at the start of the cycle
      }
      return slow; //
    }
  }
  return null;
};

// D = the distance from the beginning of the linked list to the node that starts the cycle
// P = the distance from the node that starts the cycle to the position where the slow pointer equals the fast pointer
// R = the remaining distance from P back to D
// slow = D + P
// fast = D + 2P + R
// fast = 2 * slow
// D + 2P + R = 2 * (D + P)
// R = D
