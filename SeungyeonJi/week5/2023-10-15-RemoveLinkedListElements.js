let removeLinkedListElements = function (head, val) {
  let dummy = new ListNode();
  dummy.next = head;

  let leader = dummy;
  let cur = head;

  while (cur) {
    let nxt = cur.next;

    if (cur.val == val) {
      leader.next = nxt;
    } else {
      leader = cur;
    }
    cur = nxt;
  }
  return dummy.next;
};
