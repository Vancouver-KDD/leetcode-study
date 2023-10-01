func totalFruit(_ fruits: [Int]) -> Int {
    if fruits.count <= 2 {
        return fruits.count
    }
    var basket: [Int: Int] = [:]
    var startIndex = 0
    var result = 0
    for (index, fruit) in fruits.enumerated() {
        if basket[fruit] == nil && basket.count == 2 {
            //현재 과일이 Basket에 없고, 바스켓에 이미 2개의 과일이 들어있다.
            //새 과일이 바스켓에 들어와함
            
            result = max(result, index - startIndex)
            //새 과일이 들어올때, 전 과일들의 갯수를 result에 저장해줌
            
            let priviousFruits = fruits[index - 1]
            let otherFruit = basket.keys.first { $0 != priviousFruits }!
            //현재 인덱스(새로운과일)의 이전 인덱스에 있는 과일 말고 다른 과일을 찾는다.
            
            startIndex = basket[otherFruit]! + 1
            //startIndex는 다른 과일의 + 1 부터임
            
            basket[otherFruit] = nil
            //다른과일은 버리기
            
            basket[fruit] = index
            //현재 과일 인덱스 저장
        }
        basket[fruit] = index
        //다른 과일이 나올대 까지 현재 과일의 마지막 인덱스 계속 저장
    }
    return max(result, fruits.count - startIndex)
}
