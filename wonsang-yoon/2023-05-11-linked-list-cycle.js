/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    //set up two pointer to find if two points are meeting at the same point
    let f_pointer = head;
    let s_pointer = head;
    //while the next pointer is alive
    while(f_pointer && f_pointer.next){
        //declare variables and declare one varaible one ahead to catch next pointer
        f_pointer = f_pointer.next.next;
        s_pointer = s_pointer.next
        if(f_pointer === s_pointer)
            return true
    }
    return false;
};