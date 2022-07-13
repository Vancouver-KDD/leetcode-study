function canJump(nums){
  let reachable = 0;
  
  for(let i = 0; i < nums.length; i++){
    if(reachable < i) return false;
    reachable = Math.max(reachable, i + nums[i]);
  }
  return true;
}