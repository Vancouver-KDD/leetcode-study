var reverseList = function (head) {
  let cur = head;
  let prev = null;
  let next;

  while (cur !== null) {
    next = cur.next;
    cur.next = prev;
    prev = cur;
    cur = next;
  }

  return prev;
};
