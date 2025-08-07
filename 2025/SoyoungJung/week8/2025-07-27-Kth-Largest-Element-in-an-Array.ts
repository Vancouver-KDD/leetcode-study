export class ListNode {
  val: number;
  next: ListNode | null;

  constructor(val?: number, next?: ListNode | null) {
    this.val = val ?? 0;
    this.next = next ?? null;
  }
}

export class MinHeap {
  heap: ListNode[];

  constructor() {
    this.heap = [];
  }

  push(node: ListNode) {
    this.heap.push(node);
    this.bubbleUp();
  }

  pop(): ListNode | undefined {
    const top = this.heap[0];
    const end = this.heap.pop();
    if (this.heap.length > 0 && end) {
      this.heap[0] = end;
      this.bubbleDown();
    }
    return top;
  }

  isEmpty(): boolean {
    return this.heap.length === 0;
  }

  private bubbleUp() {
    let index = this.heap.length - 1;
    const element = this.heap[index];

    while (index > 0) {
      const parentIdx = Math.floor((index - 1) / 2);
      const parent = this.heap[parentIdx];
      if (element.val >= parent.val) break;
      this.heap[parentIdx] = element;
      this.heap[index] = parent;
      index = parentIdx;
    }
  }

  private bubbleDown() {
    let index = 0;
    const length = this.heap.length;
    const element = this.heap[0];

    while (true) {
      let leftIdx = 2 * index + 1;
      let rightIdx = 2 * index + 2;
      let smallest = index;

      if (
        leftIdx < length &&
        this.heap[leftIdx].val < this.heap[smallest].val
      ) {
        smallest = leftIdx;
      }
      if (
        rightIdx < length &&
        this.heap[rightIdx].val < this.heap[smallest].val
      ) {
        smallest = rightIdx;
      }

      if (smallest === index) break;

      [this.heap[index], this.heap[smallest]] = [
        this.heap[smallest],
        this.heap[index],
      ];
      index = smallest;
    }
  }
}

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
  const minHeap = new MinHeap();

  for (const node of lists) {
    if (node) minHeap.push(node);
  }

  const dummy = new ListNode(0);
  let current = dummy;

  while (!minHeap.isEmpty()) {
    const smallest = minHeap.pop()!;
    current.next = smallest;
    current = current.next;
    if (smallest.next) {
      minHeap.push(smallest.next);
    }
  }

  return dummy.next;
}
