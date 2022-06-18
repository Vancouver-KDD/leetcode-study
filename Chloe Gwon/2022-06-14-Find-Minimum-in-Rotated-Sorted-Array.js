var findMin = function(nums) {
    var left = 0;
    var right = nums.length-1;
    
    if (nums.length === 1){
        return nums[0];
    }
    
    while (left < right){
        var midPoint = left + Math.floor((right - left) / 2);
        
        if (nums[midPoint] > nums[right]){
            left = midPoint+1;
        } else if (nums[midPoint] < nums[right]){
            right = midPoint;
        }
    }
    return nums[left];
};
