
// 206. Reverse Linked List
// Given the head of a singly linked list, reverse the list, and return the reversed list.



var reverseLinkedList = (head) =>{
    let current = null;
    while(head) {
        let next = head.next;
        head.next = current;
        current = head;
        head = next;
    }
    return current;

    //T.C : O(N) while loop with checking linked list
    //S.C : O(1) No extra space needed
}