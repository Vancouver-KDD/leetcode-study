function splitListToParts(head: ListNode | null, k: number): Array<ListNode | null> {
    const result = []
    let len = 0
    let copy = head
    while (copy) {
        copy = copy.next
        len++
    }
    copy = head
    let i
    let remainder = len % k
    let sub = Math.floor(len / k)
    console.log(remainder, sub)
    let temp
    for (i = 0; i < k; i++) {
        let j = remainder && copy ? 0 : 1
        if (remainder) {
            remainder--
        }
        for (j; j < sub && copy; j++) {
            copy = copy.next
        }
        temp = copy
        if (copy) {
            copy = copy.next
            temp.next = null
        }
    }
    return result
}
