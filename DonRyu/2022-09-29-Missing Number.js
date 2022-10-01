let missingNumber = function(nums) {
    let numsSum = 0;
    let corrSum = 0;
    for (let i = 0; i < nums.length + 1; i++) {
        corrSum += i;
        numsSum += i < nums.length ? nums[i] : 0;
    }
    return corrSum - numsSum;
};

