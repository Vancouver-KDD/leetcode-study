// Given the head of a singly linked list, reverse the list, and return the reversed list.
// Input: head = [1,2,3,4,5]
// Output: [5,4,3,2,1]

var reverseList = function(head) {
   let cur = head;
   let prev = null;
   while(cur) {
    let holdNext = cur.next;
    cur.next = prev;
    prev = cur;
    cur = holdNext;
   }
   return prev;
}