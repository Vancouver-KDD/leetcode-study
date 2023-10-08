func intervalIntersection(_ firstList: [[Int]], _ secondList: [[Int]]) -> [[Int]] {
    guard !(firstList.isEmpty || secondList.isEmpty) else { return [] }
    var firstIndex = 0
    var secondIndex = 0
    var resultArray: [[Int]] = []
    
    while firstIndex < firstList.count && secondIndex < secondList.count {
        let start = max(firstList[firstIndex][0], secondList[secondIndex][0])
        let end = min(firstList[firstIndex][1], secondList[secondIndex][1])
        
        if end >= start {
            resultArray.append([start, end])
        }
        
        if  end == firstList[firstIndex][1] {
            firstIndex += 1
        }
        
        if  end == secondList[secondIndex][1] {
            secondIndex += 1
        }
    }
    return resultArray
}
