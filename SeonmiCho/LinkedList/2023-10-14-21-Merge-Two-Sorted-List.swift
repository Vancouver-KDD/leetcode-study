func mergeTwoLists(_ list1: ListNode?, _ list2: ListNode?) -> ListNode? {
    if list1 == nil || list2 == nil { return list1 == nil ? list2 : list1 }
    if list1!.val <= list2!.val {
        list1?.next = mergeTwoLists(list1?.next, list2)
        return list1
    } else {
        list2?.next = mergeTwoLists(list1, list2?.next)
        return list2
    }
}
