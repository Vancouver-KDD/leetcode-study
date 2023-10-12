/*
 * https://leetcode.com/problems/add-two-numbers-ii/
 * 
 * ## Description
 * You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains 
 * a single digit. Add the two numbers and return the sum as a linked list.
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 * 
 * ## Example 
 * Input: l1 = [7,2,4,3], l2 = [5,6,4], Output: [7,8,0,7]
 */


class Solution {
    public ListNode addTwoNumbers(ListNode num1, ListNode num2) {
        //Create dummy node to store the return value. 
        //ans will go through all the nodes, so at the end of all process, it will be at the end of the nodes.
        //therefore, we need to store res in advance to return the value from the beginning of the linked list. (after reversal) 
        ListNode ans = new ListNode(); 
        ListNode res = ans; 
				
        //Will store the 0 or 1 depends on the sum of two numbers exceeds 10 or not. 
        int count = 0; 
				
        //We need to reverse the number so we could sum up two number from the nd (just same as the proper addition)
        ListNode l1 = reverse(num1);
        ListNode l2 = reverse(num2); 
				
        //Iterate until both of the numbers become null 
        while (l1 != null || l2 != null) {
            //Will store the sum of two numbers 
            int sum = 0; 
            
            //add the number and move to the next node for next iteration 
            if(l1 != null) {
                sum += l1.val; 
                l1 = l1.next;
            }

            if(l2 != null) {
                sum += l2.val; 
                l2 = l2.next; 
            }
						
            //add count in case there was the sum exceeding 10 in the previous iteration. 
            sum += count; 
            //store the remainder in case the sum is exceeding 10. 
            ans.next = new ListNode(sum % 10);
            ans = ans.next; 
            //store the quotient in case the sum is exceeding 10. 
            count = sum / 10; 
        }
				
        //after loop, if the last sum was exceeding 10, we need to add a node at the end. 
        if(count == 1) { 
            ans.next = new ListNode(count); 
        }
				
        //reverse the list as a return value. 
        return reverse(res.next);

    }

    //Reverse method 
    public static ListNode reverse(ListNode node){
        ListNode prev = null , temp ;
        while(node != null){
            temp = node.next;
            node.next = prev;
            prev = node;
            node  = temp;
        }
        return prev;
    }
}