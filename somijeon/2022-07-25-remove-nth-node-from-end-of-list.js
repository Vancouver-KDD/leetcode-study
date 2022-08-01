// Given the head of a linked list, remove the nth node from the end of the list and return its head.

// Example 1:

// Input: head = [1,2,3,4,5], n = 2
// Output: [1,2,3,5]

// Example 2:

// Input: head = [1], n = 1
// Output: []

var removeNthFromEnd = function (head, n) {
  let pointer1 = head;
  let pointer2 = head;

  for (let i = 0; i < n; i++) {
    pointer2 = pointer2.next;
  }

  if (!pointer2) {
    return head.next;
  }

  while (pointer2.next) {
    pointer1 = pointer1.next;
    pointer2 = pointer2.next;
  }

  pointer1.next = pointer1.next.next;

  return head;
};
