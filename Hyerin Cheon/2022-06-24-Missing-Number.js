function missingNumber(nums){
  const mySet = new Set(nums);
  for(let number = 0; number < nums.length + 1; number++){
    if(!mySet.has(number)){
      return number;
    }
  }
}