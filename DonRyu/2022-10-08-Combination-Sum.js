var combinationSum = function(candidates, target, combination = [], sum = 0 , result = [] , start = 0) {
    // Base condition
    if(sum === target){
        result.push(combination)
    }
    // Optimizing... If sum is greater than target, then other iteration of recursion are prevented
    if(sum > target) {
        return
    }
    // Assign i to start to avoid duplicates
    for(let i = start; i < candidates.length; ++i) {
      // Sum increased by each i'th value. This is calculated for each branch exploration
      sum += candidates[i]
      combinationSum(candidates, target, [...combination, candidates[i]], sum, result, i )
      // Sum decreased by each i'th value. This is calculated for each back tracking
      sum -= candidates[i]
    }

    return result
};
