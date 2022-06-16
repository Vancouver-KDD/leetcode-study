var search = function(nums, target) {
    var left = 0;
    var right = nums.length - 1;
    
    while (left < right){
        var mid = Math.floor((left + right) / 2);
        if (nums[mid] === target) return mid;
        
        //Left portion is in the ascending order
        if (nums[left] <= nums[mid]){
            if (target >= nums[left] && target < nums[mid]) {
                right = mid;
            }else {
                left = mid + 1;
            }
        } else { //Right portion is in the ascending order
            if (target > nums[mid] && target <= nums[right]) {
                left = mid + 1;
            }else{
                right = mid;
            }
        }
    }
    
    return nums[left] === target ? left : -1;
};
