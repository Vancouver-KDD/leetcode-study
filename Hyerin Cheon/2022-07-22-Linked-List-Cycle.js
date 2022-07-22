function hasCycle(head){
  // start point
  let fast = head;
  let slow = head;

  while(fast && fast.next){
    // fast moves two steps
    fast = fast.next.next;
    // slow moves one step
    slow = slow.next;

    if(fast === slow) return true;
  }
  return false;
}
