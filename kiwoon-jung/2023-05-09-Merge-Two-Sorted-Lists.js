var mergeTwoLists = function (L1, L2) {
  const dummy = new ListNode(-Infinity);
  let prev = dummy;

  while (L1 && L2) {
    if (L1.val <= L2.val) {
      prev.next = L1;
      prev = L1;
      L1 = L1.next;
    } else {
      prev.next = L2;
      prev = L2;
      L2 = L2.next;
    }
  }

  if (!L1) prev.next = L2;
  if (!L2) prev.next = L1;

  return dummy.next;
};
