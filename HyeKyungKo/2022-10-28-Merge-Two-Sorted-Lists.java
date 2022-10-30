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

//Time Complexity: O(n+m) <- n: size of list1, m : size of list2
//Space Complexity: O(1)
class Solution{
    public ListNode mergeTwoLists(ListNode list1, ListNode list2){
        
        ListNode head = new ListNode();
        ListNode merged = head;
        while(list1 != null || list2 != null){
            if(list1 == null){
                merged.next = list2;
                break;
            }else if(list2 == null){
                merged.next = list1;
                break;
            }else{
                if(list1.val <= list2.val){
                    merged.next = list1;
                    list1 = list1.next;
                }else{
                    merged.next = list2;
                    list2 = list2.next;
                }
                merged = merged.next;
            }            
        }
        
        return head.next;
    }
}