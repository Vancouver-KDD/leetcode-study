var missingNumber = function(nums) {
    nums.sort((a,b) => a - b)
    for (i = 0; i <= nums.length; i++) {
        if (i !== nums[i]) return i;
    }
};