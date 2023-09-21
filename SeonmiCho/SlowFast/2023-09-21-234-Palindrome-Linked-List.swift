func reverse(_ head: ListNode?) -> ListNode? {
    var head = head
    var pre: ListNode? = nil
    
    while head != nil {
        let next = head?.next   //next = ListNode(2, ListNode(3, nil))   //ListNode(3, nil)
        head?.next = pre        //head = ListNode(1, nil)                //ListNode(2, ListNode(1, nil))
        pre = head              //pre = ListNode(1, nil)                 //pre = ListNode(2, ListNode(1, nil))
        head = next             //head = ListNode(2, ListNode(3, nil))   //head = ListNode(3, nil)
    }
    
    return pre
}


func isPalindrome(_ head: ListNode?) -> Bool {
    //fast는 slow의 두배씩 움직인다.
    //fast가 끝에 도달하면 slow는 절반이다.
    var slow = head
    var fast = head
    
    while fast != nil && fast?.next != nil {
        fast = fast?.next?.next
        slow = slow?.next
    }
    
    if fast != nil { //fast가 nil이 아니면 가운데 값이 있는 palindrome 이므로 slow를 한칸 더 옮겨줌
        slow = slow?.next
    }
    
    slow = reverse(slow)
    fast = head
    while slow != nil {
        if slow?.val != fast?.val {
            return false
        }
        slow = slow?.next
        fast = fast?.next
    }
    return true
    
}
