var rob = function(nums){
  if(!nums.length) return 0;
  if(nums.length === 1) return nums[0];
  if(nums.length === 2) return Math.max(nums[0], nums[1]);

  // return if we start at first house or skip it (start from second house)
  return Math.max(helper(nums.slice(0, nums.length - 1)), helper(nums.slice(1)));
};

// used the same logic as house robber 1
function helper(segment){
  if(segment === null || segment.length === 0) return 0;

  let dp = new Array(segment.length);
  dp[0] = segment[0]
  dp[1] = Math.max(segment[0], segment[1]);
  
  for(let i = 2; i < segment.length; i++){
    dp[i] = Math.max(dp[i - 2] + segment[i], dp[i - 1]);
  }
  return dp[segment.length - 1];
}