// You are given the head of a singly linked-list. The list can be represented as:

//* L0 → L1 → … → Ln - 1 → Ln
//todo: Reorder the list to be on the following form:

//todo: L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
// You may not modify the values in the list's nodes. Only nodes themselves may be changed.

// Ex 1:
// Input: head = [1,2,3,4]
// Output: [1,4,2,3]

// Ex 2:
// Input: head = [1,2,3,4,5]
// Output: [1,5,2,4,3]

var reorderList = function (head) {
  if (!head || !head.next || !head.next.next) return head;

  let [fast, slow] = [head.next, head];
  while (fast && fast.next) {
    [fast, slow] = [fast.next.next, slow.next];
  }

  const secondHalf = slow.next;

  slow.next = null;

  let [curr, prev] = [secondHalf, null];
  while (curr) {
    [curr.next, prev, curr] = [prev, curr, curr.next];
  }

  while (prev) {
    [head.next, prev.next, head, prev] = [prev, head.next, head.next, prev.next];
  }
};
