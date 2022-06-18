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

//Better solution
var maxProduct = function(nums) {
    var min = nums[0];
    var max = nums[0];
    var result = nums[0];
    
    for (var i=1; i<nums.length; i++){
        
        var tempMax = Math.max(nums[i]*max, Math.max(nums[i]*min, nums[i]));
        min = Math.min(nums[i]*max, Math.min(nums[i]*min, nums[i]));
        
        max = tempMax;
        result = Math.max(result, max);
    }
    return result;
};
