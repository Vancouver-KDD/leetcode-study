func minDepth(_ root: TreeNode?) -> Int {
    guard root != nil else { return 0 }
    var result = Set<Int>()
    getDepth(root, &result, 1)
    return result.min() ?? 0
}

func getDepth(_ root: TreeNode?, _ result: inout Set<Int>, _ depth: Int) {
    guard root != nil else { return }
    
    if root!.left == nil && root!.right == nil {
        result.insert(depth)
    }
    
    if let left = root!.left {
        getDepth(left, &result, depth + 1)
    }
    
    if let right = root!.right {
        getDepth(right, &result, depth + 1)
    }
}
