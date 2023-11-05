func canPartition(_ nums: [Int]) -> Bool {
    let sum = nums.reduce(0, +)
    if sum % 2 != 0 || nums.count == 1 {
        return false
    }
    let target = sum / 2
    //sum / 2가 우리의 target이다 => 합이 똑같은 어레이를 찾아야하니까
    
    var dp = Array(repeating: false, count: target + 1)
    //0부터 target 까지 표기해야하기 때문에 target + 1 이다.
    //if target is 4, => 0,1,2,3,4
    
    dp[0] = true
    //합이 0이 되는 부분 배열이 항상 존재한다고 초기화 한다.
    
    for num in nums {
        for i in stride(from: target, through: num, by: -1) {
            dp[i] = dp[i] || dp[i - num]
        }
    }
    return dp[target]
    //dp[target]이 true 면 부분 배열이 있는것.
}
