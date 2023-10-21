func rightSideView(_ root: TreeNode?) -> [Int] {
    var result: [Int] = []
    helper(root, &result, 0)
    return result
}

func helper(_ head: TreeNode?, _ result: inout [Int], _ depth: Int) {
    guard head != nil else { return }
    
    if result.count == depth { //현재 뎁스가, result의 count와 같으면 추가
        result.append(head!.val)
    }
    helper(head!.right, &result, depth + 1) //helper 한번 돌때마다 depth 추가
    helper(head!.left, &result, depth + 1)
}
