var hasCycle = function(head) {
    var slow = head;
    var fast = head;
    while (slow && fast) {
      slow = slow.next;
      fast = fast.next ? fast.next.next : undefined;
      if (slow === fast) return true;
    }
    return false;
  };
