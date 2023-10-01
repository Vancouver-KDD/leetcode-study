func longestSubstring(_ s: String, _ k: Int) -> Int {
    guard s.count >= k else {
        return 0
    }
    // Store the Strings Count
    let count: [Character: Int] = s.reduce(into: [:]) { $0[$1, default: 0] += 1 }
    // O(n)
    
    var dividers: [Int] = []
    var result = 0
    
    // Make a divider
    for (index, character) in s.enumerated() {
        if count[character]! < k {
            dividers.append(index)
            //To know where the divider
        }
    }
    
    // If the count of divider is empty,
    // It means that all of characters are satisfied with the condition.
    if dividers.count == 0 {
        return s.count
        // We can return the count of input s
    }
    
    // Divid input string
    var startIndex = s.startIndex
    for index in dividers {
        // We need to know the end index this area.
        // 'endIndex' is the index that each divider.
        let endIndex = s.index(s.startIndex, offsetBy: index)
        
        // if the for loop coutinues well, the count will be return on line 22.
        // So we need to compare the count result
        // Max can find the greatest value
        let area = s[s.startIndex..<endIndex]
        result = max(result, longestSubstring(String(area), k))
        startIndex = s.index(s.startIndex, offsetBy: index + 1)
        // And we need to find next divider,
        // So we will change the start Index to next index of current divider.
    }
    // last loop => we need one more loop btween last divider and end of string
    result = max(result, longestSubstring(String(s[startIndex...]), k))
    return result
}
