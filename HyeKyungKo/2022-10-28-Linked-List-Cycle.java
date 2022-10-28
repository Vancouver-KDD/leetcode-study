//Similar question
//  142. Linked List Cycle II (premium ??)

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */

//Floyd's Cycle Finding Algorithm
//Time Complexity: O(n)
//Space Complexity: O(1)
public class Solution{
    public boolean hasCycle(ListNode head){
        
        ListNode slow = head; //each step - one move
        ListNode fast = head; //each step - two move
        
        while(fast!= null && fast.next != null){ //only need to check fast.
            slow = slow.next;
            fast = fast.next.next;
            if(slow == fast){
                return true;
            }
            
        }
        
        return false;
    }
}

//Time Complexity: O(n)
//Space Complexity: O(n)
/*
public class Solution {
    public boolean hasCycle(ListNode head) {
        
        if(head == null || head.next == null ){
            return false;
        }
        
        HashSet<ListNode> nodeSet = new HashSet<>();
        
        while(head !=null){
            if(nodeSet.contains(head)){
                return true;
            }
            nodeSet.add(head);
            head = head.next;
        }
        
        return false;
    }
}
*/