/*
 처음에 생각한 간단한 방법
 map으로 Square Array로 만든 후 정렬
 아마 시간 복잡도가 증가할 것 같음
 */

func sortedSquares(_ nums: [Int]) -> [Int] {
    return nums.map { $0 * $0 }.sorted()
}


/*
 two pointer를 사용한 방법
 */
func sortedSquares(_ nums: [Int]) -> [Int] {
    var right = nums.count - 1
    var left = 0
    var result = nums
    var index = right
    
    while index >= 0 {
        if abs(nums[left]) < abs(nums[right]) {
            result[index] = nums[right] * nums[right]
            right -= 1
        } else {
            result[index] = nums[left] * nums[left]
            left += 1
        }
        index -= 1
    }
    return result
}
