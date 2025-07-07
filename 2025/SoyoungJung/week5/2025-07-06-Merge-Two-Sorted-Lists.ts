class MergeTwoListsListNode {
  val: number;
  next: MergeTwoListsListNode | null;
  constructor(val?: number, next?: MergeTwoListsListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function mergeTwoLists(
  list1: MergeTwoListsListNode | null,
  list2: MergeTwoListsListNode | null
): MergeTwoListsListNode | null {
  if (list1 === null) return list2;
  if (list2 === null) return list1;

  if (list1.val < list2.val) {
    list1.next = mergeTwoLists(list1.next, list2);
    return list1;
  } else {
    list2.next = mergeTwoLists(list1, list2.next);
    return list2;
  }
}
