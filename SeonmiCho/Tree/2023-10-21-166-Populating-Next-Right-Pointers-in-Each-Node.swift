func connect(_ root: Node?) -> Node? {
    //넓이우선 탐색을 이용해야한다.
    //넓이 우선 탐색은 Queue를 이용한다.
    //맨처음 시작 노드를 Queue에 넣는다.
    //시작 노드를 방문했다면 방문처리를 해준다.
    //큐에서 노드를 하나 꺼낸다.
    //해당노드에 연결된 노드 중 방문하지 않았던 노드를 방문하고 차례로 Queue에 삽입한다.
    //루트에서 가까운것 부터 가게 됨
    
    var left = root
    
    while left != nil {
        var head = left
        while head != nil {
            head?.left?.next = head?.right
            if let next = head?.next {
                head?.right?.next = next.left
            }
            head = head?.next //줄바꿈이라고 보면됨
        }
        left = left?.left
    }
    return root
}
