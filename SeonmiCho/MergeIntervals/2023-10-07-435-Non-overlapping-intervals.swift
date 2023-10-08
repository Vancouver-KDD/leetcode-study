func eraseOverlapIntervals(_ intervals: [[Int]]) -> Int {
    if intervals.count < 3 {
        return 0
    }
    
    let sortedInterval = intervals.sorted { $0[1] < $1[1] }
    
    var previous = 0
    var count = 1
    
    //병합 하려면 뒤의 최소값이 전의 최대값보다 작다.
    for index in 1..<sortedInterval.count {
        if sortedInterval[index][0] >= sortedInterval[previous][1] {
            previous = index;
            count += 1
        }
    }
    return sortedInterval.count - count
}
