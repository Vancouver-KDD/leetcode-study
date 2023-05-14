/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode MergeTwoLists(ListNode list1, ListNode list2) {

        ListNode prev = new ListNode();
        ListNode head = prev;
        while(list1!=null && list2!=null){
            if(list1.val > list2.val){
                prev.next = list2;
                list2 = list2.next;
            }
            else{
                prev.next = list1;
                list1 = list1.next;
            }
            prev = prev.next;
        }

        if(list1 !=null){
            prev.next = list1;
        }
        if(list2 !=null){
            prev.next = list2;
        }   

        return head.next;     
    }
}
//TC: O(N)
//SC: O(1)
