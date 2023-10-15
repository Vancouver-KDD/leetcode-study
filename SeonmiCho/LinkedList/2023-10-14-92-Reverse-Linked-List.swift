func reverseBetween(_ head: ListNode?, _ left: Int, _ right: Int) -> ListNode? {
    guard head?.next != nil else { return head }
    guard left < right else { return head }
    
    //고정되는 값
    var leftStartNode = head
    
    //움직일 노드
    var currentNode = leftStartNode
    
    var leftTailNode: ListNode? = nil
    var midTailNode: ListNode? = nil
    var index = 1
    
    //Current Node를 움직여서 뒤집어져야할 시작점 체크 및 나중에 이어야할 부분 체크
    while index < left {
        leftTailNode = currentNode //나중에 뒤집힌거 이어야할 부분
        currentNode = currentNode?.next
        index += 1
    }
    
    midTailNode = currentNode
    var node0 = midTailNode //얘가 뒤집힌애
    var node1 = node0?.next //얘가 끝난 뒤집힌 지점 이후 시작점
    var node2 = node1?.next
    
    while index < right {
        // 여기서 노드를 뒤집어 줘야함
        node1?.next = node0
        node0 = node1
        node1 = node2
        node2 = node2?.next
        index += 1
    }
    
    if leftTailNode == nil {
        midTailNode?.next = node1 //leftTail이 없는 경우 뒤만 연결
        return node0 // 뒤집힌 노드 뒤에 나머지 노드 붙여서 리턴
    } else {
        leftTailNode?.next = node0 //leftTail에 뒤집힌 노드 연결
        midTailNode?.next = node1  //뒤집힌 노드에 나머지 연결
        return leftStartNode //헤드 리턴
    }
}
