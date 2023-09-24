// Given the head of a singly linked list, return true if it is a palindrome
// or false otherwise.
// Follow up: Could you do it in O(n) time and O(1) space?

//* Example 1:

// Input: head = [1,2,2,1]
// Output: true

//* Example 2:

// Input: head = [1,2]
// Output: false

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function (head) {
  // Edge case: an empty list or a list with a single node is a palindrome
  if (!head || !head.next) {
    return true;
  }
  // slow and fast starts from the same point
  let slow = head;
  let fast = head;
  let stack = [];

  // Find the middle of the list using the slow and fast pointers
  while (fast !== null && fast.next !== null) {
    // fast.next !== null is for the case of odd number of nodes
    stack.push(slow.val);
    slow = slow.next;
    fast = fast.next.next;
  }

  // If the list has an odd number of nodes, skip the middle node
  if (fast !== null) {
    slow = slow.next;
  }

  // Check if the slow of the list matches the elements in the stack
  while (slow !== null) {
    if (slow.val !== stack.pop()) {
      return false;
    }
    slow = slow.next;
  }

  return true;
};

console.log(isPalindrome([1, 2, 3, 4]));
