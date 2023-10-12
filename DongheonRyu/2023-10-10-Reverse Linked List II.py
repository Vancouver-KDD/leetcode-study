def reverseBetween(left,right):
    dummy = ListNode(0,head)

    leftPrev,cur = dummy,head
    for i in range(left - 1):
        leftPrev,cur = cur, cur.next

    prev = None
    for i in range(right-left+1):
        tmpNext = cur.next
        cur.next = prev
        prev,cur = cur, tmpNext

    leftPrev.next.next = cur
    leftPrev.next = prev

    return dummy.next
