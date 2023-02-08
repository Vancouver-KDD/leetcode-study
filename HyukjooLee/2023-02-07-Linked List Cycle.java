/// how to detect the cycle?
 // think about the next pointer of nodes

// 1. using slow and fast pointers
// if there is a cycle in the linked list, fast pointer will catch up the slow pointer 
// loop the list until fast != slow
// and if fast pointer is null or there is no node linked with, it means linked list is not cycled
// time complexity is O(N) as we traverse the head node; the length of the linked list 
public class Solution {
    public boolean hasCycle(ListNode head) {
        // slow and fast pointers
        // fast pointer will catch up the slow pointer 
        // if there is a cycle in the linked list
        if(head == null || head.next == null) return false;
        ListNode fast = head.next;
        ListNode slow = head;
        while(fast != slow) {
            if(fast == null || fast.next == null) {
                return false;
            }
            // move two pointers
            fast = fast.next.next;
            slow = slow.next;
        }
        return true;
    }
}

// 2. using hashset
// why not using hashmap?
// main purpose is to store each node's reference(hash), not key or value
// you encounter a node that is already in the set,
// then you know there is a cycle in the list
public class Solution {
    public boolean hasCycle(ListNode head) {
        HashSet<ListNode> set = new HashSet<>();
        while(head != null) {
            if(set.contains(head)) {
                return true;
            } else {
                set.add(head);
            }
            head = head.next;
        }
        return false;
    }
}
