// Given head, the head of a linked list,
// determine if the linked list has a cycle in it.

// There is a cycle in a linked list if there is some node in the list that can be reached again
// by continuously following the next pointer. 
// Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
// Note that pos is not passed as a parameter.

// Return true if there is a cycle in the linked list. Otherwise, return false.

// how to detect the cycle?
// think about the next pointer of nodes

// 1. using slow and fast pointers
// if there is a cycle in the linked list, fast pointer will catch up the slow pointer 
// loop the list until fast != slow
// and if fast pointer is null or there is no node linked with, it means linked list is not cycled
// time complexity is O(N) as we traverse the head node; the length of the linked list 
// space complexity is O(1), as it does not create any additional data structures; e.g. hashset
// only need slow and fast pointers
// memory used remains constant; not rely on the size of linkedlist

// Review
// 한 노드씩 순환하는 slow pointer
// 두 노드씩 순환하는 fast pointer 를 활용해서
// fast pointer 가 null 또는 fast.next 가 null 일때, false 를 리턴 (listnode 가 순환되기 않고 끝난다는 의미기 때문에)
// 만약 fast 노드가 slow 노드를 따라잡으면
// cycle 이 있다는 의미
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
// time complexity is O(n) - to traverse every nodes of list when there is no cycle or all nodes are distinct
// space complexity is O(n) - to store each reference of node, we created hashset

// Review
// nodes 를 한 포인터씩 옮기면서 특정 노드가 이미 hash set 에 있는지 확인하고
// 없다면 node 의 고유한 값을 저장함
// 있으면 cycle 이 있다는 의미
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
