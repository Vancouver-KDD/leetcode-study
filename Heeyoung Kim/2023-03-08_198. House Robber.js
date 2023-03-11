var rob = function(nums){
    if(nums.length === 0) return 0;
    if(nums.length === 1) return nums[0];
    if(nums.length === 2) return Math.max(nums[0], nums[1]);

    let output = [nums[0], Math.max(nums[0], nums[1])];

    for(let i=2; i<nums.length; i++){
        output.push(Math.max(nums[i] + output[i-2], output[i-1]));
    }

    return output.pop();
}