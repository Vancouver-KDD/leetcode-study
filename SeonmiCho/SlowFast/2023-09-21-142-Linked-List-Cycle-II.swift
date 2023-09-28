
func detectCycle(_ head: ListNode?) -> ListNode? {
    var slow = head
    var fast = head
    
    repeat {
        slow = slow?.next
        fast = fast?.next?.next
        if fast == nil || slow == nil {
            return nil
        }
        guard slow !== fast else { break }
        //fast와 slow가 만났다고 해서 거기가 순환의 시작지점인 것은 아니다. 그냥 만남 지점이고, 순환리스트라는 것
    } while fast?.next?.next != nil && slow?.next != nil
    
    slow = head
    //slow를 처음으로 보내준다.
    
    while fast !== slow {
        slow = slow?.next
        fast = fast?.next
    }
    //fast 와 slow가 다시 처음 만나는 지점이 순환의 시작 지점이다. 순환의 길이와 관련있음.
    return slow
}
