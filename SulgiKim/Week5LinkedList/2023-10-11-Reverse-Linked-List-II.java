/*
 * https://leetcode.com/problems/reverse-linked-list-ii/
 * 
 * ## Description
 * Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position 
 * right, and return the reversed list.
 * 
 * ## Example 
 * Input: head = [1,2,3,4,5], left = 2, right = 4, Output: [1,4,3,2,5]
 */


class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        //Set early exit conditions 
        if (head == null) {
            return null; 
        }
        if (head.next = null) {
            return head; 
        }

        ListNode prev = null;
        ListNode curr = head; 

        //Reach to the beginning of the list that need to be reversed. 
        //After the loop, curr pointer should be at the exact start point, prev should be the node right before beginning. 
        while(left > 1) { // same aws for (int i = 1; i < left; i++)
            prev = curr; 
            curr = curr.next;
            left--;
            right--; // decrement the right pointer as well for next while loop. 
        }

        //Store the prev and curr to connect with reversed list later. 
        ListNode connection = prev; 
        ListNode tail = curr; 

        //Reverse the list only until reach to the right 
        //At the end, prev will be the head of the reversed list, curr will be the next node of the prev 
        while(right > 0) {
            ListNode next = curr.next;
            curr.next = prev; 
            prev = curr; 
            curr = next; 
            right--; 
        }  

        //connect the head of reversed list with any other nodes that has been left before reversing
        if(connection != null) {
            connection.next = prev; 
        } else { //if connection = null, means that left was 1 and the reversed list was starting at the very beginning of the original linked list. 
            head = prev; 
        }
        //connect the tail of reversed list with any other nodes that has been left after reversing 
        tail.next = curr;

        return head; 
    }
}