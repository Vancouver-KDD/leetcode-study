/* https://leetcode.com/problems/reorder-list/description/
 * 
 * ## Description  
 * 
 * You are given the head of a singly linked-list. The list can be represented as:

    L0 → L1 → … → Ln - 1 → Ln
    Reorder the list to be on the following form:

    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
    You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 * To solve this question, we need to be able to access from the end of linked list backward. 
 * 1. Place a pointer to the middle 
 * 2. Reverse the back half of the list. 
 * 3. Place the pointers to both ends of list 
 * 4. Converge the pointers while merge the front and back half lists like the example in description. 
 */

class Solution {
    public void reorderList(ListNode head) {
        //Set the slow & fast pointers to the beginning of the linked list
        ListNode slow = head, fast = head; 
        
        //Using slow and fast pointers, place the slow pointer at the middle and fast pointer at the end of list. 
        while (fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next; 
        }

        //Reverse back half of the list 
        ListNode reversedNode = reverse(slow.next); 
        
        //Break the list in the middle 
        slow.next = null; 

        while (reversedNode != null) {
            //Initialize the temporary variables to store the next element from the both ends. 
            ListNode temp1 = head.next;
            ListNode temp2 = reversedNode.next; 

            //Link the nodes as we need to 
            head.next = reversedNode; 
            reversedNode.next = temp1; 

            //Move the pointers to the next element
            head = temp1;
            reversedNode = temp2; 
        }


    }


    //Reversal process 
    public ListNode reverse(ListNode node){
        ListNode prev = null; //to break the reversal loop 

        while(node != null){
            ListNode temp = node.next;
            node.next = prev; 
            prev = node;
            node = temp; 
        }

        return prev; 
    }
}