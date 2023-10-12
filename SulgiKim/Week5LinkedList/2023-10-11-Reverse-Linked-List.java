/*
 * https://leetcode.com/problems/reverse-linked-list/
 * 
 * ## Description 
 * Given the head of a singly linked list, reverse the list, and return the reversed list.
 * 
 * ## Example 
 * Input: head = [1,2,3,4,5] , Output: [5,4,3,2,1]
 */


class Solution {
    public ListNode reverseList(ListNode head) {
        //Set the break point for reversed linked list 
        ListNode prev = null;

        while(head != null) {
            //Initialize temporary node to store the next node and link after change the direction. 
            ListNode tmp = head.next;
            //reverse the direction 
            head.next = prev;
            //move to the next node for next process 
            prev = head;
            //move to the next node for next process 
            head = tmp;
        }

        return prev;
    }
}