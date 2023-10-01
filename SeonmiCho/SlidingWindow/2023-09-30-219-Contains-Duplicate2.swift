
func containsNearbyDuplicate(_ nums: [Int], _ k: Int) -> Bool {
    //1. brute force - 해결은 할 수 있을 것 같으나, nums의 크기가 클때 시간이 오래걸리게된다.
    // for (iIndex, i) in nums.enumerated() {
    //     for (jIndex, j) in nums.enumerated() where iIndex != jIndex {
    //         if i == j && abs(iIndex - jIndex) <= k {
    //             return true
    //         }
    //     }
    // }
    
    
    //기준(k)을 넘은 인덱스는 버리면서 가는게 좋지않을까
    var count: [Int: Int] = [:]
    for (index, value) in nums.enumerated() {
        if count[value] != nil {
            if !(abs(count[value]! - index) <= k) {
                count[value] = nil
            } else {
                return true
            }
        }
        count[value] = index
    }
    
    return false
}
