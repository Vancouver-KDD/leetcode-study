/*
 two pointer에서는 정렬이 중요한듯
 */

func threeSumClosest(_ nums: [Int], _ target: Int) -> Int {
    let sortedNums = nums.sorted()
    let endIndex = sortedNums.count - 1
    var diff: Int = .max
    var result = 0
    
    for i in 0...endIndex {
        var base = sortedNums[i]
        var left = i + 1
        var right = endIndex
        
        while left < right {
            let sum = base + sortedNums[left] + sortedNums[right]
            
            if sum > target {
                //Sum이 목표값보다 크다 -> 더 작은 값을 찾기 위해 오른쪽 포인터를 옮긴다.
                right -= 1
            } else {
                //Sum이 목표값보다 작다 -> 더 큰 값을 찾기 위해 오른쪽 포인터를 옮긴다.
                left += 1
            }
            
            let value = abs(sum - target)
            
            if value < diff {
                diff = value
                result = sum
            }
        }
    }
    return result
}
