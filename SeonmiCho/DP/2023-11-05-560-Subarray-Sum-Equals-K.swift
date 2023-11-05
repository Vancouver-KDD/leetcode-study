func subarraySum(_ nums: [Int], _ k: Int) -> Int {
    //WINDOW
    // var count = 0
    // var left = 0
    // var right = 0
    // var currentSum = 0
    
    // if nums.count == 1, nums.first == k {
    //     return 1
    // }
    
    // while right < nums.count {
    //     currentSum += nums[right]
    
    //     if currentSum == k {
    //         count += 1
    //         right += 1
    //     } else {
    //         right += 1
    //     }
    
    //     if right >= nums.count {
    //         left += 1
    //         right = left
    //         currentSum = 0
    //     }
    // }
    // return count
    
    //[1, 1, 1], k = 2
    //prefixSumCount = [0: 2, -1: 1, 1: 1]
    
    //DP
    var prefixSumCount: [Int: Int] = [0: 1]
    var count = 0
    var currentSum = 0
    
    for num in nums {
        currentSum += num
        let diff = currentSum - k
        if let prefixCount = prefixSumCount[diff] {
            count += prefixCount
        }
        
        prefixSumCount[currentSum, default: 0] += 1
    }
    return count
}
