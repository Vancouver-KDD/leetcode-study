func constructMaximumBinaryTree(_ nums: [Int]) -> TreeNode? {
    guard !nums.isEmpty else { return nil }
    let headIndex = getIndexOfLargestNumber(nums)
    var left = Array(nums[..<headIndex])
    var right = Array(nums[(headIndex + 1)...])
    var head = TreeNode(nums[headIndex])
    head.left = constructMaximumBinaryTree(left)
    head.right = constructMaximumBinaryTree(right)
    return head
}

func getIndexOfLargestNumber(_ nums: [Int]) -> Int {
    var result = 0
    var resultIndex = 0
    for (index, num) in nums.enumerated() {
        if result < num {
            result = num
            resultIndex = index
        }
    }
    return resultIndex
}
