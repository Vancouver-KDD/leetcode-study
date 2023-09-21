class Solution {
    func hasCycle(_ head: ListNode?) -> Bool {
        var slow = head
        var fast = head
        
        repeat {
            slow = slow?.next
            fast = fast?.next?.next
            if slow == nil, fast == nil {
                break
            }
            guard slow !== fast else {
                return true
            }
        } while fast?.next?.next != nil
        
        return false
    }
}
