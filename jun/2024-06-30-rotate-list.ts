function rotateRight(head: ListNode | null, k: number): ListNode | null {
    let len = 1
    let tail = head
    if (!head?.next) {
        return head
    }
    while (tail.next) {
        tail = tail.next
        len++
    }
    tail.next = head

    k = k % len

    let temp = head
    for (let i = 1; i < len - k; i++) {
        temp = temp.next
    }

    const newHead = temp.next
    temp.next = null

    return newHead
}
