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
 //2023.02.05
 //2022.11.04
 //Time Complexity: O(n)
 //Space Complexity: O(1)
class Solution{
    public void reorderList(ListNode head){
        
        ListNode slow = head; //move one step
        ListNode fast = head; //move two step

        //find middle node
        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;  
        }

        //reverse the second list (from middle node to end node)
        ListNode second = reverseList(slow);
        ListNode first = head;

      
        
        //merge two lists
        ListNode temp;
        while(second.next != null){ // if second list reach the end, stop 
            temp = first.next;
            first.next = second;
            first = temp;

            temp = second.next; 
            second.next = first;
            second = temp;
        }
    }

    private ListNode reverseList(ListNode head){
        ListNode pre = null;
        ListNode next = null;
        while(head != null){
            next = head.next;
            head.next = pre;
            pre = head;
            head = next;
        }
        
        return pre;
    }
}

 //Time Complexity: O(n)
 //Space Complexity: O(n)
 /*
class Solution {
    public void reorderList(ListNode head) {
        if(head == null || head.next == null){
            return;
        }

        ListNode mNode = head;
        int count = 0;
        HashMap<Integer, ListNode> map = new HashMap<>();
        while(mNode != null){
            map.put(count, mNode);
            count++;
            mNode = mNode.next;
        }

        int i = 0;
        ListNode dummyNode = new ListNode(0);

        while(i <= count/2){
            ListNode first = map.get(i);
            ListNode second = map.get(count -1 -i);
            if(first == second){ // middle node in case of odd number,
                dummyNode.next = first;
                dummyNode = dummyNode.next;
            }else{
                dummyNode.next = first;
                dummyNode.next.next = second;
                dummyNode = dummyNode.next.next;
            }

            i++;
        }
        dummyNode.next = null;

    }
}
*/