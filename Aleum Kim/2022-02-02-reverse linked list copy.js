const reverseList = (head) => {
    let previous = null
    let current = head
    while(current) {
        const next = current.next
        current.next = previous
        previous = current
        current = next
    }
    return previous
}
