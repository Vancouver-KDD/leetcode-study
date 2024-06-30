var maximumSubarraySum = function (nums, k) {
    let currHash = new Map();
    let currArr = nums.slice(0, k);
    for (let i = 0; i < currArr.length; i++) {
        currHash.set(currArr[i], (currHash.get(currArr[i]) || 0) + 1)
    }
    let currentSum = currArr.reduce((acc, cur) => acc + cur, 0);
    let max = currHash.size === k ? Math.max(currentSum, 0) : 0;

    for (let i = k; i < nums.length; i++) {
        currHash.set(nums[i - k], currHash.get(nums[i - k])-1);
        if (currHash.get(nums[i - k]) === 0) {
            currHash.delete(nums[i - k]);
        }
        currHash.set(nums[i], (currHash.get(nums[i]) || 0) + 1);
        currentSum = currentSum - nums[i - k] + nums[i]
        if (currHash.size === k) {
            max = Math.max(currentSum, max);
        }
    }

    return max;
};
