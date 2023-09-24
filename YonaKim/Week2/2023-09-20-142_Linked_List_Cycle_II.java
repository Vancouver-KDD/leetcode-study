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

 //ArrayList.contains() -> O(n) time complexity
 //HashSet.contains() -> O(1) time complexity

public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode dummy = head;
        HashSet<ListNode> hashSet = new HashSet<>();

        while(dummy != null) {
            if(hashSet.contains(dummy)) {
                return dummy;
            }

            hashSet.add(dummy);
            dummy = dummy.next;
        }

        return null; 
    }
}