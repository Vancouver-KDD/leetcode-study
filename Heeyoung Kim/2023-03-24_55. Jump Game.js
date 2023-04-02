var canJump = function(nums) {
    let idx = 0;
    let max = 0;
    let target = nums.length -1;
    
    while(idx < nums.length) {
        max = Math.max(max, idx+nums[idx]);
        
        if(max >= target) { return true; }
        if(max <= idx && nums[idx] === 0) { return false; }
        
        idx++;
    }
    return false;
};