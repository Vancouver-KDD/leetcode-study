/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    if (nums.length === 1) return nums[0];
    if (nums.length === 2) return Math.max(nums[0], nums[1]);
    
    var currMax = nums[0];
    var maxSum = Math.max(nums[0], nums[1]);
    
    for (var i=2; i<nums.length; i++) {
        var temp = maxSum;
        maxSum = Math.max(currMax + nums[i], maxSum);
        currMax = temp;
    }
    
    return maxSum;
};

