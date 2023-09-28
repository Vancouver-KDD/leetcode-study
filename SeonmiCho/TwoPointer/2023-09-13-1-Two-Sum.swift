/**
 TwoPointer
 일단 정렬해서 합을 찾은 뒤 각 숫자의 인덱스를 찾아서 리턴하는 방법
 */
func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
    let sortedNums = nums.sorted()
    var left = 0
    var right = nums.count - 1
    
    while left < right {
        let sum = sortedNums[left] + sortedNums[right]
        if target == sum {
            if let firstIndex = nums.firstIndex(of: sortedNums[left]),
               let lastIndex = nums.lastIndex(of: sortedNums[right]) {
                return [firstIndex, lastIndex]
            }
        } else {
            if sum > target {
                right -= 1
            } else {
                left += 1
            }
        }
    }
    return []
}


/**
 딕셔너리를 활용한 좋은 방법
 */
func twoSum(_ nums: [Int], _ target: Int) -> [Int] {
    var dict: [Int: Int] = [:]
    
    //index와 element를 함께 받음
    for (index, num) in nums.enumerated() {
        //dict에 값이 없다면 target - num 한 값을 key로 하는 index를 저장한다.
        //나중에 루프롤 돌다가 이전에 target - num으로 저장한 값이 딕셔너리에 있다면
        //합이 target과 같은것이므로, 이전에 저장했던 index와, 현재 돌고있는 index를 함께 리턴한다
        if let indexForNum = dict[num] {
            return [indexForNum, index]
        } else {
            dict[target - num] = index
        }
    }
    return []
}
