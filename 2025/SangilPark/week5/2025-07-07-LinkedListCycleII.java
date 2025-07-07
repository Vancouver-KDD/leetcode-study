package week5;
import java.util.*;

/*
 * Week 5: Linked List
 * https://leetcode.com/problems/linked-list-cycle-ii/
 */
class Solution {
    public static ListNode detectCycle(ListNode head) {
        if (head == null || head.next == null) {
            return null;
        }

        List<ListNode> nodes = new ArrayList<>();
        ListNode pointer = head;

        while (pointer != null) {
            nodes.add(pointer);
            pointer = pointer.next;
            
            if (nodes.contains(pointer)) {
                return nodes.get(nodes.indexOf(pointer));
            }
        }
        return null;
    }

    public static void main(String[] args) {
        int[] input = {1,2,3,4,5};
        ListNode head = new ListNode(1);
        detectCycle(head);
    }

    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
}