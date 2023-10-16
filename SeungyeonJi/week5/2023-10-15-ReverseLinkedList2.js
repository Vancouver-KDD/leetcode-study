var reverseBetween = function (head, left, right) {
  const dummy = new ListNode(0);

  dummy.next = head;
  let leader = dummy;

  for (let i = 0; i < left - 1; i++) {
    leader = leader.next;
  }

  let cur = leader.next;

  for (let i = 0; i < right - left; ++i) {
    let nodeToBeExt = cur.next;
    cur.next = nodeToBeExt.next;
    nodeToBeExt.next = leader.next;
    leader.next = nodeToBeExt;
  }

  return dummy.next;
};
