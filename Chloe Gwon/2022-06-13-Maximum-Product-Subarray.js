var maxProduct = function(nums) {
    var curMax = nums[0];
    var curMin = nums[0];
    var finalMax = nums[0];
    
    for (var i=1; i<nums.length; i++){
        var temp = curMax;
        curMax = Math.max(nums[i], curMax*nums[i], curMin*nums[i]);
        curMin = Math.min(nums[i], temp*nums[i], curMin*nums[i]);
        finalMax = Math.max(finalMax, curMax);
    }
    
    return finalMax;
};
