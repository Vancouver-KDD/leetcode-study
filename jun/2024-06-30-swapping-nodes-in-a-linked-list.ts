function swapNodes(head: ListNode | null, k: number): ListNode | null {
    if (!head.next) {
        return head
    }
    let len = 1
    let temp = head
    while (temp.next) {
        temp = temp.next
        len++
    }
    temp = head
    let temp2 = head
    let a, b
    let i = 1

    const [first, second] = [Math.min(k, len - k + 1), Math.max(k, len - k + 1)]
    while (i < first) {
        temp = temp.next
        temp2 = temp2.next
        i++
    }
    a = temp.val
    while (i < second) {
        temp = temp.next
        i++
    }
    b = temp.val
    temp.val = a
    temp2.val = b
    return head
}
