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
        
        ListNode node = new ListNode();
         ListNode head = new ListNode();
        head = node;
        
        while(list1 != null && list2 != null){
            if(list1.val > list2.val){
                node.next = list2;
                list2=list2.next;
            }else{
                node.next = list1;
                list1=list1.next;
            }       
            node = node.next;
        }
        node.next = list1!=null?list1 : list2;
        return head.next;
        
        
    }
}