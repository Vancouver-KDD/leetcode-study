function remoceNthFromEnd(head, n){
  let dummyHead = new ListNode(-Infinity);
  dummyHead.next = head;

  // need to reference for the output since the dummyHead is increment all the way
  let resultHead = dummyHead;

  let tail = head;
  let count = 0;

  // move tail by n
  while(count < n){
    tail = tail.next;
    count++;
  }

  let removeNode = head;
  let prev = dummyHead;

  while(tail){
    tail = tail.next;
    removeNode = removeNode.next;
    prev = prev.next;
  }
  // if tail is null
  // break the pointer and link to new node
  prev.next = removeNode.next;

  return resultHead.next;
}