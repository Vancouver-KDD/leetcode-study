class ReverseListListNode {
  val: number;
  next: ReverseListListNode | null;
  constructor(val?: number, next?: ReverseListListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function reverseList(
  head: ReverseListListNode | null
): ReverseListListNode | null {
  let prev: ReverseListListNode | null = null;
  let curr = head;

  while (curr !== null) {
    const nextTemp = curr.next;
    curr.next = prev;
    prev = curr;
    curr = nextTemp;
  }

  return prev;
}
