function reverseList(head){
  let curr = head;
  let prev = null;
  let next = null;

  while(curr){
    // set next and save
    next = curr.next;

    // make it reverse, change the pointer way
    curr.next = prev;

    // move prev to curr and curr to next
    prev = curr;
    curr = next;
  }
  return prev;
}