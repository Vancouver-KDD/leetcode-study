₩₩₩
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        // 1) 사이클 유무 확인
        ListNode slow = head;
        ListNode fast = head;
        
        while (fast != null && fast.next != null) {
            slow = slow.next;          // 한 칸
            fast = fast.next.next;     // 두 칸
            if (slow == fast) {        // 만남 확인
                // 2) 사이클 시작점 찾기
                ListNode ptr1 = head;
                ListNode ptr2 = slow;  // 만난 지점
                while (ptr1 != ptr2) {
                    ptr1 = ptr1.next;
                    ptr2 = ptr2.next;
                }
                return ptr1;          // 사이클의 시작 노드
            }
        }
        
        // 사이클이 없으면 null 반환
        return null;
    }
}
₩₩₩
