const detectCycle = function (head) {
  if (!head || !head.next) return null;

  let slowPointer = head;
  let fastPointer = head;

  while (fastPointer && fastPointer.next) {
    slowPointer = slowPointer.next;
    fastPointer = fastPointer.next.next;

    if (slowPointer === fastPointer) {
      let middlePointer = head;
      while (slowPointer !== middlePointer) {
        slowPointer = slowPointer.next;
        middlePointer = middlePointer.next;
      }
      return slowPointer;
    }
  }

  return null;
};
