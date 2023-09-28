/*
 * https://leetcode.com/problems/linked-list-cycle-ii/description/
 * 
 * ##Description 
 * 
 * Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
 * 
 * Using Floyd's Cycle Detection ALgorithm along with slow and fast pointers. 
 * Floyd's Cycle Detection Algorithm :
 *  - If there is a cycle in linked list, the fast pointer will eventually catch up the slow pointer. 
 *      - When slow and fast pointer meet, the distance between head & the entering point to the cycle is the same 
 *                              as the distance between where slow and fast pointer meet and the entering point to the cycle 
 *  - If there is no cycle in linked list, the fast pointer will reach the end of linked list 
 * 
 */

public class Solution {
    public ListNode detectCycle(ListNode head) {
        //Set the pointer to at the beginning of the linked list
        ListNode slow = head, fast = head; 

        // Move the pointer while checking if there is a cycle 
        while (fast != null && fast.next != null ) { //Check for both cases (odd and even numbers of nodes in linked list)
            slow = slow.next;
            fast = fast.next.next;
            
            //If the slow and fast pointer meet, there is a cycle. 
            if (slow == fast) {
                //Find the entering point to cycle 
                while (head != slow) { //we can also use fast that is moving instead of slow, since they are at the same node. 
                    head = head.next;
                    slow = slow.next; 
                }

                return head; 
            }
        }

        //if fast reaches the end of node, there is no cycle. 
        return null; 
    }
}