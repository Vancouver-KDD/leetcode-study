```
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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // 더미 노드로 시작
        ListNode dummy = new ListNode(-1);
        ListNode tail = dummy;
        
        // 두 리스트를 모두 순회하면서 작은 값을 갖는 노드를 tail 뒤에 붙인다
        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                tail.next = list1;
                list1 = list1.next;
            } else {
                tail.next = list2;
                list2 = list2.next;
            }
            tail = tail.next;
        }
        
        // 남아 있는 노드를 한 번에 붙인다
        tail.next = (list1 != null) ? list1 : list2;
        
        // dummy.next가 병합된 리스트의 실제 헤드
        return dummy.next;
    }
}
₩₩₩
