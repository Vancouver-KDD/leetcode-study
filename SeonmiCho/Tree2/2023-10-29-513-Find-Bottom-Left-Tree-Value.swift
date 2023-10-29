func findBottomLeftValue(_ root: TreeNode?) -> Int {
    guard root != nil else { return 0 }
    var result: [Int] = []
    var currentDepth: Int = 0
    
    if root!.left == nil, root!.right == nil {
        return root!.val
    }
    
    func findLeft(_ root: TreeNode?, _ depth: Int) {
        guard root != nil else { return }
        //가장 깊은 레벨중에 가장 왼쪽을 찾아야함
        
        if currentDepth < depth {
            currentDepth = depth
            result = []
        }
        
        if depth >= currentDepth {
            result.append(root!.val)
        }
        findLeft(root!.left, depth + 1)
        findLeft(root!.right, depth + 1)
        
    }
    findLeft(root, 0)
    return result.first ?? 0
}
