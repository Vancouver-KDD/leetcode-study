function lengthOfLIS(nums){
  let dp = new Array(nums.length).fill(1);
  let longest = 1;

  for(let i = 1; i < nums.length; i++){
    for(let j = 0; j < i; j++){
      if(nums[j] < nums[i]){
        dp[i] = Math.max(nums[i], 1 + nums[j]);
        longest = Math.max(dp[i], longest);
      }
    }
  }
  return longest;
}