let hasCycle = function (head) {
  let slowPt = head;
  let fastPt = head;

  while (fastPt && fastPt.next) {
    slowPt = slowPt.next;
    fastPt = fastPt.next.next;

    if (slowPt === fastPt) return true;
  }
  return false;
};
