
func reverseList(_ head: ListNode?) -> ListNode? {
    guard head?.next != nil else { return head }
    var head = head
    var pre: ListNode? = nil
    
    while head != nil {
        let next = head?.next
        head?.next = pre
        pre = head
        head = next
    }
    return pre
}
