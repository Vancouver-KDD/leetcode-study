function reorderList(head){
  // for exceptional
  if(!head) return;

  let second = split(head);
  second = reverse(second);
  merge(head, second);
};

function split(node){
  let fast = node;
  let slow = node;

  // finding the middle of the linked list
  while(fast){
    if(fast.next && fast.next.next){
      slow = slow.next;
      fast = fast.next.next;
    } else {
      fast = null;
    }
  }

  const secondHalf = slow.next;
  // split
  slow.next = null;
  
  return secondHalf;
}

// reverse second list
function reverse(node) {
  let prev = null;
  let curr = node;
  
  while(curr){
    let next = curr.next;
    curr.next = prev;

    prev = curr;
    curr = next;
  }
  return prev;
}

// merge two lists
function merge(l1, l2){
  let l1Next = null;
  let l2Next = null;

  while(l2){
    // reference, cuz its value will be changing
    l1Next = l1.next;
    l2Next = l2.next;

    l1.next = l2;
    l2.next = l1Next;

    l1 = l1Next;
    l2 = l2Next;
  }
}