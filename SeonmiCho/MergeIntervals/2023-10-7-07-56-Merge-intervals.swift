
func merge(_ intervals: [[Int]]) -> [[Int]] {
    let sorted = intervals.sorted(by: { $0[0] < $1[0] })
    var result: [[Int]] = []
    var previous: [Int] = sorted[0]
    var index = 1
    
    while index < sorted.count {
        if previous[0] <= sorted[index][0] && previous[1] >= sorted[index][0] {
            previous = [previous[0], max(sorted[index][1], previous[1])]
        } else {
            result.append(previous)
            previous = sorted[index]
        }
        index += 1
    }
    result.append(previous)
    return result
}
