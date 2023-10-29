func diameterOfBinaryTree(_ root: TreeNode?) -> Int {
    var max = 0
    getHeight(root, &max)
    return max
}

func getHeight(_ root: TreeNode?, _ result: inout Int) -> Int {
    //노드 길이의 합이 가장 큰 걸 찾으면 될듯
    //중복되는 경로를 제거해야함
    guard root != nil else { return 0 }
    let left = getHeight(root!.left, &result)
    let right = getHeight(root!.right, &result)
    result = max(result, left + right)
    //max를 쓰는거 -> 더 깊은 노드를 찾는거
    //만약 result 보다 left + right 가 더 크면 이전보다 더 깊은 노드가 있는거
    return max(left, right) + 1 //depth가 더 긴쪽에 length 추가
    
    //내가 처음 했더 방식은 중복되는 경로를 거를 수 없었음, 근데 max를 쓰면 중복되는 경로를 거를 수 있다.
}
