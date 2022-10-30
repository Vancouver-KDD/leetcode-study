/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
//one pass algorithm
//Time Complexity: O(n)
//Space Complexity: O(1)
//ListNode dummy와 first, second copynode 를 이용
class Solution{
    public ListNode removeNthFromEnd(ListNode head, int n){
        
        ListNode tempNode = new ListNode();
        tempNode.next = head;
        ListNode first = tempNode;
        ListNode second = tempNode;
        
        int count = 0; 
        //make the n node gap between first and second
        while(first != null && count <= n){ 
            first = first.next;
            count++;
        }
        
        //move to the position the (n-1)th node from the end of the list
        while(first != null){
            first = first.next;
            second = second.next;
        }
        second.next = second.next.next;
        
        return tempNode.next;
    }
}

    
//Two pass algorithm
//Time Complexity: O(n) <-- O(2n) 이여서 O(n) 
//Space Complexity: O(1)
/*
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        
        ListNode removedList = head;

        int listSize = 0;
        
        while(removedList != null){
            listSize++;
            removedList = removedList.next;
        }
        
        removedList = head;
        
        int count = listSize - n;
        
        if(count < 0){
            return head; // n is worng number
        }else if(count == 0){
            return head.next; // remove first node. 
        }
        count--; // need to stop before the node to remove
        while(count > 0){
            removedList = removedList.next;
            count--; 
        }
        
        removedList.next = removedList.next.next;
        
        return head;
    }
}
*/