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

//Time Complexity: O(N)
//Space Complexity: O(1)

//A linked list can be reversed either iteratively or recursively. Could you implement both?

//2023-10-09 -iteratively
//Time Complexity: O(N)
//Space Complexity: O(1)

class Solution{
    public ListNode reverseList(ListNode head){
        if(head == null || head.next == null){
            return head;
        }
        
        ListNode prevNode = null;
        ListNode currNode = head;
        while(currNode != null){
            ListNode nextNode = currNode.next;
            currNode.next = prevNode;
            prevNode = currNode;
            currNode = nextNode;
        }
        
        return prevNode;
    }
}

//2023-10-09- Recursively - leetcode 의 solution 방식
//Time Complexity : O(N)
//Space Complexity: O(N) -  The extra space comes from implicit stack space due to recursion. The recursion could go up to n levels deep.
/*
class Solution{
    public ListNode reverseList(ListNode head){
        if(head == null || head.next == null){
            return head;
        }
        
        ListNode nextNode = head.next;
        ListNode reverseHead = reverseList(nextNode);
        nextNode.next = head;
        head.next = null;
            
        return reverseHead;
    }
}
*/
//2023-10-09- Recursively - 내가 푼 방식 
//Time Complexity : O(N)
//Space Complexity: O(N) -  The extra space comes from implicit stack space due to recursion. The recursion could go up to n levels deep.
/*
class Solution{
    public ListNode reverseList(ListNode head){
        if(head == null || head.next == null){
            return head;
        }
        
        return recursiveReverseList(head, null);
    }
    
    ListNode recursiveReverseList(ListNode currNode, ListNode prevNode){
        if(currNode == null){
            return prevNode;
        }
        
        ListNode nextNode = currNode.next;
        currNode.next = prevNode;
        return recursiveReverseList(nextNode, currNode);
    }
}
*/
