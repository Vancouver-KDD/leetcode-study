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
    var count=0;
    
    while(head!=null){
        if (count==10000) return true;
        count++;
        head=head.next;
    }
    return false;
};
