var missingNumber = function(nums) {
    var res = 0;
    var n = nums.length;
    var rangeSum = (n * (n+1)) / 2;
    
    for (var i=0; i<nums.length; i++){
        res += nums[i];
    }
    
    return (rangeSum - res);
};
