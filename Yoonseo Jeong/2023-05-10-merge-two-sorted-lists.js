var mergeTwoLists = function(list1, list2) {
    if(!list1 && !list2) return null
    if (!list1) return list2
    if (!list2) return list1

    // make head node, since we can't specify which head of the list is smaller
    // create dummy data of node to start connecting to next
    const result = new ListNode(0, null)
    // current node to track
    let current = result

    // loop until one of the list is empty
    while(list1 && list2) {
        // compare item value
        // if list1 is smaller or equal
        if(list1.val <= list2.val) {
            current.next = list1
            list1 = list1.next
        }
        else {
            current.next = list2
            list2 = list2.next
        }
        // make current to be added data
        current = current.next
    }
    
    // put the rest of remaining to next
    current.next = list1 || list2

    // return result without first head node with dummy data
    return result.next

    // complexity
    // time: O(n+m)
    // space: O(n+m)
};