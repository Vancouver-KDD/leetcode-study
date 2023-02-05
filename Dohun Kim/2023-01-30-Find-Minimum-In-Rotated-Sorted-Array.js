/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    let [left, right] = [0, nums.length - 1];

    while (left < right) {
        const mid = (left + right) >> 1;
        const [leftNum, rightNum] = [nums[left], nums[right]];
        if (leftNum <= rightNum) return leftNum;
        if (leftNum <= nums[mid]) left = mid + 1;
        if (nums[mid] < leftNum) right = mid;
    }

    return nums[left];
};