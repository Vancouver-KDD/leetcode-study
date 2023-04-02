// 143. Reorder List
// You are given the head of a singly linked-list. The list can be represented as:

// L0 → L1 → … → Ln - 1 → Ln
// Reorder the list to be on the following form:

// L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
// You may not modify the values in the list's nodes. Only nodes themselves may be changed.

var reorderList = function(head) {
    let middle = findMiddle(head);
    let list2 = reverse(middle.next);
    middle.next = null;

    merge(head, list2);

    
};

// 1. Find Middle => To divide the array (linkedList)
let findMiddle = (head) => {
    //slow or fast pointer 
    let slow = head;
    let fast = head;
    while(fast && fast.next) {
        slow = slow.next;
        fast = fast?.next?.next
    }
    
    return slow;
}

//2. Reverse => To reverse array2 

let reverse = (head) => {
    let previous = null;
    let current = head;

    while(current) {
        let next = current.next;
        current.next = previous;
        previous = current;
        current = next;
    }
    return previous;
}

//3. Merge => To merge List 1 and List 2 

let merge = (list1, list2) => {
    while(list2) {
        let next = list1.next;
        list1.next = list2;
        list1 = list2;
        list2 = next;
    }
    //result linkedlist 를 안씀으로써 S.C 는 O(1)
}

//Time Complexity : O(N) 
//Space Complexity : O(1)