```
public ListNode reverseList(ListNode head) {
    ListNode prev = null;
    ListNode curr = head;

    while (curr != null) {
        // (1) 다음 노드 주소 보관
        ListNode nextTemp = curr.next;
        // (2) 포인터 뒤집기
        curr.next = prev;
        // (3) 포인터 한 칸씩 전진
        prev = curr;
        curr = nextTemp;
    }
    // prev가 새 헤드
    return prev;
}

```
