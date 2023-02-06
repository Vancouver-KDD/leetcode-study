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

 //2023-02-05
 //Time Complexity: O(N+M) -> N is size of list1, M is size of list2
 //Space Complexity: O(1)
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {

        ListNode dummyHead = new ListNode();
        ListNode currNode;
        currNode = dummyHead;

        while(list1 != null && list2 != null){
            if(list1.val < list2.val){
                currNode.next = list1;
                list1 = list1.next;
            }else{
                currNode.next = list2;
                list2 = list2.next;
            }
            currNode = currNode.next;
        }

        if(list1 == null ){
            currNode.next = list2;
        }else{
            currNode.next = list1;
        }

        return dummyHead.next;
    }
}