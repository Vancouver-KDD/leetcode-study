// 1. using for two loops 
// O(n^2)
var containsDuplicate = function(nums){
  for(let firstNum = 0; firstNum < nums.length; firstNum++){
    for(let secondNum = firstNum + 1; secondNum < nums.length; secondNum++){
      if(nums[firstNum] === nums[secondNum]){
        return true;
      }
    }
  }
  return false;
}

// 2. using Set()
// O(n)
var containsDuplicate = function(nums){
  const mySet = new Set();
  for(let i = 0; i < nums.length; i++){
    if(mySet.has(nums[i])){
      return true;
    }
    mySet.add(nums[i])
  }
  return false;
}