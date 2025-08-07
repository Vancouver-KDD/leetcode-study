```
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        // Min-heap ordering nodes by val
        PriorityQueue<ListNode> pq = new PriorityQueue<>(
            Comparator.comparingInt(node -> node.val)
        );
        
        // Push the head of each non-null list
        for (ListNode node : lists) {
            if (node != null) {
                pq.offer(node);
            }
        }
        
        // Dummy head to build result list
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        
        // Extract-min and push next until empty
        while (!pq.isEmpty()) {
            ListNode minNode = pq.poll();
            tail.next = minNode;
            tail = tail.next;
            if (minNode.next != null) {
                pq.offer(minNode.next);
            }
        }
        
        return dummy.next;
    }
}


```
