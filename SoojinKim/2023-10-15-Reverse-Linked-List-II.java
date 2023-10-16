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
class Solution {
    ListNode th=null;
    ListNode tt=null;
    void addFirst(ListNode node){
        if(th==null){
            th=node;
            tt=node;
        }
        else{
            node.next=th;
            th=node;
        }
    }
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if(head==null || head.next==null) return head;
        ListNode curr = head;
        ListNode prev = null;
        int count=1;
        while(curr!=null){
            while(count>=left && count<=right){
                ListNode fwd = curr.next;
                curr.next=null;
                addFirst(curr);
                curr=fwd;
                count++;
            }
            if(count>right){
                if(prev!=null){
                    prev.next=th;
                    tt.next=curr;
                    return head;
                }
                else{
                    tt.next=curr;
                    return th;
                }
            }
            count++;
            prev=curr;
            curr=curr.next;
        }
        return head;
    }
}